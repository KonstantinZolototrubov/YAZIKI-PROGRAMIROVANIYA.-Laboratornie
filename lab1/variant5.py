order_name = input("Название заказа: ")
customer_name = input("Имя заказчика: ")

item1 = input("Название первой позиции: ")
count1 = int(input("Количество: "))
price1 = float(input("Цена за единицу: "))

item2 = input("Название второй позиции: ")
count2 = int(input("Количество: "))
price2 = float(input("Цена за единицу: "))

delivery = float(input("Стоимость доставки: "))
discount_percent = float(input("Скидка в процентах (0-100): "))
paid = float(input("Внесённая сумма: "))

#вычисления
sum1 = count1 * price1
sum2 = count2 * price2
goods = sum1 + sum2
discount_rub = goods * (discount_percent / 100)
total = (goods - discount_rub) + delivery
total_count = count1 + count2
change = paid - total

#вывод
print("\n" + "=" * 40)

print("ЗАКАЗ:", order_name)
print("Заказчик:", customer_name)

print("=" * 40)

print(item1, "|", count1, "| {:.2f}".format(price1), "| {:.2f}".format(sum1))
print(item2, "|", count2, "| {:.2f}".format(price2), "| {:.2f}".format(sum2))

print("-" * 40)

print("Стоимость товаров: {:.2f}".format(goods))
print("Скидка: {:.2f}".format(discount_rub))
print("Итого с доставкой: {:.2f}".format(total))
print("Общее количество: ", total_count)
print("Сдача: {:.2f}".format(change))

print("=" * 40)
