# Project: Multiplication Table
# Lesson: 10
# Author: Evgeny
# Date: 17.07.2026

x = int(input("Введите число: "))

print(f"\nТаблица умножения для числа {x}\n")

for i in range(1, 11):
    print(f"{x} × {i} = {x * i}")
