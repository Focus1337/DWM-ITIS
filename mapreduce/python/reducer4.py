#!/usr/bin/env python3

import sys

# Текущий ключ и сумма цен
current_key = None
total_price = 0

# Читаем входные данные из стандартного потока ввода
for line in sys.stdin:
    # Удаляем начальные и конечные пробелы и разделяем строку на ключ и значение
    key, value, _, _ = line.strip().split('\t')

    # Если текущий ключ отличается от предыдущего, выводим результат
    if current_key and current_key != key:
        print(f"{current_key}\t{total_price}")

        # Сбрасываем сумму для нового ключа
        current_key = key
        total_price = 0

    # Обновляем текущий ключ и сумму цен
    current_key = key
    total_price += float(value)

# Выводим последний результат
if current_key:
    print(f"{current_key}\t{total_price}")