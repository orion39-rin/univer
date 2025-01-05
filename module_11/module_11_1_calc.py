import time  # Для измерения времени выполнения
from multiprocessing import Pool  # Для реализации многопроцессного подхода

# Функция для обработки файла
def process_file(filename):
    """
    Открывает файл, считывает его содержимое, преобразует символы в числа (ASCII-коды),
    выполняет сложные вычисления с числами.
    Аргументы:
        filename (str): Имя файла для обработки.
    """
    results = []  # Локальный список для хранения результатов вычислений
    with open(filename, 'r', encoding='utf-8') as file:  # Открываем файл
        while True:
            line = file.readline()  # Считываем строку
            if not line:  # Если строка пустая, заканчиваем чтение
                break
            # Преобразуем каждый символ строки в ASCII-код и выполняем сложные вычисления
            computed_values = [((ord(char) ** 3) // 7) % 100 for char in line.strip()]
            results.extend(computed_values)  # Сохраняем результаты вычислений
    # Итоговый список results нигде не возвращается, так как задача демонстрационная
    # и нас интересует только производительность выполнения операций.

if __name__ == '__main__':
    # Список названий файлов. Измените на реальные файлы в вашей директории.
    filenames = [f'file {num}.txt' for num in range(1, 5)]  # Например, file 1.txt, file 2.txt и т.д.

    # *** Линейный подход ***
    print("Линейный вызов:")
    start_time = time.perf_counter()  # Засекаем начальное время
    for filename in filenames:
        process_file(filename)  # Последовательно обрабатываем каждый файл
    end_time = time.perf_counter()  # Засекаем конечное время
    print(f"Время выполнения (линейно): {end_time - start_time:.6f} секунд")

    # *** Многопроцессный подход ***
    print("\nМногопроцессный вызов:")
    start_time = time.perf_counter()  # Засекаем начальное время
    with Pool() as pool:  # Создаём пул процессов
        pool.map(process_file, filenames)  # Параллельно обрабатываем файлы
    end_time = time.perf_counter()  # Засекаем конечное время
    print(f"Время выполнения (многопроцессно): {end_time - start_time:.6f} секунд")
