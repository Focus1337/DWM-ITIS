#!/usr/bin/env python3

import sys

current_postcode = None
total_price = 0
transaction_count = 0

# Читаем результаты от маппера из стандартного потока ввода
for line in sys.stdin:
    # Разделяем на ключ и значение
    postcode, price = line.strip().split('\t')

    # Если текущий почтовый индекс совпадает с предыдущим, добавляем цену к общей сумме и увеличиваем счетчик транзакций
    if current_postcode == postcode:
        total_price += int(price)
        transaction_count += 1
    else:
        # Если текущий почтовый индекс отличается от предыдущего, выводим результат для предыдущего почтового индекса
        if current_postcode:
            average_price = total_price / transaction_count
            print(f"{current_postcode}\t{average_price}")

        # Обновляем текущий почтовый индекс и сбрасываем счетчики
        current_postcode = postcode
        total_price = int(price)
        transaction_count = 1

# Выводим результат для последнего почтового индекса
if current_postcode:
    average_price = total_price / transaction_count
    print(f"{current_postcode}\t{average_price}")