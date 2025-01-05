# П Р О Д О Л Ж Е Н И Е
# СМОТРИ module_11_1_old.py !!!!!!!!!!!!!!!!!
"""Решение с использованием Lock"""
'''Lock предотвращает состояния гонки, но снижает параллелизм, так как только один процесс может работать с данными 
в любой момент времени. Это неизбежный компромисс между безопасностью и производительностью.'''
######################################################################################################################
from multiprocessing import Process, Manager, Lock

class WarehouseManager:
    def __init__(self):
        manager = Manager()
        self.data = manager.dict()  # Общий словарь для данных
        self.lock = Lock()  # Механизм синхронизации

    def process_request(self, request):
        product, action, amount = request

        with self.lock:  # Захватываем Lock для безопасного обновления данных
            if action == "receipt":
                self.data[product] = self.data.get(product, 0) + amount
            elif action == "shipment":
                if product in self.data and self.data[product] > 0:
                    self.data[product] = max(self.data[product] - amount, 0)

    def run(self, requests):
        processes = []
        for request in requests:
            process = Process(target=self.process_request, args=(request,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50),
    ]

    manager.run(requests)
    print(dict(manager.data))

###!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''таже шляпа
опять Чернышевский.....
смотри продолжение кровавого сериала module_11_1_old_variant_3'''

'''
......................................__.
.............................,-~*`¯lllllll`*~,
.......................,-~*`lllllllllllllllllllllllllll¯`*-,
..................,-~*llllllllllllllllllllllllllllllllllllllllllll*-,
...............,-*llllllllllllllllllllllllllllllllllllllllllllllllllllll.\.
.............;*`lllllllllllllllllllllllllll,-~*~-,llllllllllllllllllll\
..............\lllllllllllllllllllllllllll/.........\;;;;llllllllllll,-`~-,
...............\lllllllllllllllllllll,-*...........`~-~-,...(.(¯`*,`,
................\llllllllllll,-~*.....................)_-\..*`*;..)
.................\,-*`¯,*`)............,-~*`~................/
..................|/.../.../~,......-~*,-~*`;................/.\
................./.../.../.../..,-,..*~,.`*~*................*...\.
................|.../.../.../.*`...\...........................)....)¯`~,
................|./.../..../.......)......,.)`*~-,............/....|..)...`~-,.
..............././.../...,*`-,.....`-,...*`....,---......\..../...../..|.........¯```*~-,,,,
...............(..........)`*~-,....`*`.,-~*.,-*......|.../..../.../............\........
................*-,.......`*-,...`~,..``.,,,-*..........|.,*...,*...|..............\........
...................*,.........`-,...)-,..............,-*`...,-*....(`-,............\.......
......................f`-,.........`-,/...*-,___,,-~*....,-*......|...`-,..........\........'''