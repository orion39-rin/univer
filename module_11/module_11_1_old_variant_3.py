"""
Остается один выход - менять логику проги:

если мы изменим логику работы таким образом - чтобы не изменять условия задачи коренным образом - а добавим такое
понятие как запрос на товар - то есть при запросе на shipment учтем, что
если запрашивается например 100 единиц , а на складе только 30
то в результате мы записываем на склад 0 (в реальности товара не может быть меньше нуля, поэтому в задаче условие
недопущения отрицательных значений) а минус 70 мы поместим в отдельный словарь с названием запрос на товар. Этот
словарь мы также будем создавать в классе с нулевыми значениями по умолчанию. и будем обрабатывать их совместно.
при следующем поступлении товара - сначала будет гаситься запрос а при переизбытке - остаток записываться на склад.
Как будет работать предложенная логика:
При запросе на отгрузку (shipment):

Если товара хватает, то он списывается со склада.
Если товара не хватает, то остаток товара на складе обнуляется, а недостающая часть записывается в новый словарь
demand (запросы на товар).
При поступлении товара (receipt):

Сначала закрываются запросы на товар из словаря demand.
Если поступившего товара больше, чем требуется для закрытия запросов, остаток добавляется на склад.
Обработка потоков:

Мы добавим обработку и синхронизацию для работы с двумя словарями (data для склада и demand для запросов).

Добавляет новый словарь demand:
Хранит информацию о недостающем количестве товаров.
Обрабатывает запросы с учетом спроса:
При поступлении товаров сначала закрываются запросы из demand.
Обеспечивает потокобезопасность:
Используется Lock для синхронизации операций.
"""
from multiprocessing import Process, Manager, Lock

class WarehouseManagerWithDemand:
    def __init__(self):
        # Создаем менеджер и два словаря для хранения данных склада и запросов на товар
        manager = Manager()
        self.data = manager.dict()  # Словарь склада
        self.demand = manager.dict()  # Словарь запросов
        self.lock = Lock()  # Блокировка для синхронизации

    def process_request(self, request):
        product, action, amount = request

        with self.lock:  # Блокируем доступ к данным
            if action == "receipt":
                # Если товар поступает на склад
                current_demand = self.demand.get(product, 0)

                if current_demand > 0:
                    # Закрываем запросы на товар
                    if amount >= current_demand:
                        amount -= current_demand
                        self.demand[product] = 0
                    else:
                        self.demand[product] -= amount
                        amount = 0

                # Остаток записывается на склад
                if amount > 0:
                    self.data[product] = self.data.get(product, 0) + amount

            elif action == "shipment":
                # Если запрашивается отгрузка
                current_stock = self.data.get(product, 0)

                if current_stock >= amount:
                    # Если товара достаточно, списываем со склада
                    self.data[product] -= amount
                else:
                    # Если товара не хватает, создаем запрос на недостающий товар
                    self.data[product] = 0
                    self.demand[product] = self.demand.get(product, 0) + (amount - current_stock)

    def run(self, requests):
        processes = []

        for request in requests:
            process = Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

# Пример использования
if __name__ == "__main__":
    manager = WarehouseManagerWithDemand()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "shipment", 150),
        ("product1", "shipment", 50),
        ("product3", "shipment", 200),
        ("product2", "receipt", 50),
        ("product3", "receipt", 300)
    ]

    manager.run(requests)

    print("Складские запасы:", dict(manager.data))
    print("Запросы на товар:", dict(manager.demand))

###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
Логика победила гонку!
Но ....
смотри окончательный вариант module_11_1_old_variant_4.py ... ИБО....
Если важна максимальная производительность и арбайтен в реальной системе, мастхев Queue + Lock.

╔╦╦╦═╦╗╔═╦═╦══╦═╗
║║║║╩╣╚╣═╣║║║║║╩╣
╚══╩═╩═╩═╩═╩╩╩╩═╝

"""