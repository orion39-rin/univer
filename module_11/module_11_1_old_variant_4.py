#



from multiprocessing import Process, Lock, Queue

class WarehouseManagerWithQueue:
    def __init__(self):
        # Словарь для хранения текущих складских запасов
        self.data = {}
        # Словарь для хранения текущих запросов на товары
        self.demand = {}
        # Список для журнала операций
        self.log = []

        # Lock для синхронизации доступа к общим данным
        self.lock = Lock()
        # Очередь для передачи данных между процессами
        self.queue = Queue()

    def process_request(self, request):
        # Разбираем запрос: название продукта, действие, количество
        product, action, amount = request

        # Локальные словари для хранения изменений текущего процесса
        local_data = {}
        local_demand = {}
        local_log = []

        # Используем Lock для безопасного доступа к данным
        with self.lock:
            if action == "receipt":  # Обработка поступления товара
                current_demand = self.demand.get(product, 0)  # Смотрим текущий запрос на товар
                if current_demand > 0:  # Если есть запрос на этот товар
                    if amount >= current_demand:  # Если поступившего товара хватает для покрытия запроса
                        local_log.append(f"{amount} единиц {product} поступило, закрыв запрос на {current_demand} единиц.")
                        amount -= current_demand
                        local_demand[product] = 0  # Запрос закрыт
                    else:  # Если товара недостаточно для полного покрытия запроса
                        local_log.append(f"{amount} единиц {product} поступило, частично закрыв запрос на {current_demand} единиц.")
                        local_demand[product] = current_demand - amount
                        amount = 0

                if amount > 0:  # Если есть остаток после покрытия запроса
                    local_data[product] = self.data.get(product, 0) + amount
                    local_log.append(f"{amount} единиц {product} добавлено на склад.")

            elif action == "shipment":  # Обработка отгрузки товара
                current_stock = self.data.get(product, 0)  # Смотрим текущее количество на складе
                if current_stock >= amount:  # Если товара достаточно для отгрузки
                    local_data[product] = current_stock - amount
                    local_log.append(f"{amount} единиц {product} успешно отгружено.")
                else:  # Если товара недостаточно для отгрузки
                    local_log.append(f"Только {current_stock} единиц {product} отгружено. "
                                      f"Запрос на {amount - current_stock} единиц добавлен в очередь.")
                    local_data[product] = 0  # Склад опустошён
                    local_demand[product] = self.demand.get(product, 0) + (amount - current_stock)

        # Передача локальных изменений в очередь
        self.queue.put((local_data, local_demand, local_log))

    def run(self, requests):
        processes = []

        # Создаем процессы для каждого запроса
        for request in requests:
            process = Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        # Ожидаем завершения всех процессов
        for process in processes:
            process.join()

        # Сбор данных из очереди
        while not self.queue.empty():
            local_data, local_demand, local_log = self.queue.get()

            # Обновляем общий словарь складских запасов
            for key, value in local_data.items():
                self.data[key] = self.data.get(key, 0) + value

            # Обновляем общий словарь запросов
            for key, value in local_demand.items():
                self.demand[key] = value

            # Добавляем записи в общий журнал операций
            self.log.extend(local_log)

    def print_log(self):
        # Печать журнала операций
        print("\nЖурнал операций:")
        for entry in self.log:
            print(entry)

# Пример использования
if __name__ == "__main__":
    manager = WarehouseManagerWithQueue()

    # Список запросов: (название продукта, действие, количество)
    requests = [
        ("product1", "receipt", 100),
        ("product2", "shipment", 150),
        ("product1", "shipment", 50),
        ("product3", "shipment", 200),
        ("product2", "receipt", 50),
        ("product3", "receipt", 300)
    ]

    # Запуск обработки запросов
    manager.run(requests)

    # Вывод итогов
    print("\nСкладские запасы:", manager.data)
    print("Запросы на товар:", manager.demand)
    manager.print_log()

    # Записываем журнал в файл для дальнейшего анализа
    with open("log.txt", "w", encoding='utf-8') as log_file:
        for entry in manager.log:
            log_file.write(entry + "\n")

"""

┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

"""