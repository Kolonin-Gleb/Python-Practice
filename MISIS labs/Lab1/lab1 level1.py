
# task 1
'''
s = 0
for i in range(2, 35, 3):
    s += i

print(s) #187
'''

# task 2
'''
s = 0
for i in range(1, 11):
    s += (1/i)
print(s) # 2.9289682539682538
'''

# task 3
'''
s = 0
for numerator in range(2, 113, 2): # Числитель
    denominator = numerator + 1 # Знаменатель
    s += numerator / denominator

print(s) # 53.99671294118794
'''

# task 4
'''
import math

x = float(input("Введите x: "))
s = 0

for n in range(1, 10):
    s += math.cos(n * x) / (x ** (n - 1))

print(f"Значение суммы: {s}") # при x = 90 Ответ: -0.45460204393722725
'''

# task 5
'''
p = float(input("Введите p: "))
h = float(input("Введите h: "))
s = 0

for n in range(10):
    s += (p + n * h) ** 2

print(f"Сумма квадратов 10 членов ар. прогрессии: {s}")
'''

# task 6
'''
x = -4
step = 0.5

while x <= 4:
    y = 0.5 * x ** 2 - 7 * x
    print(f"x = {x} | y = {y}")
    x += step
'''

# task 7
# Вычисление факториала 6
'''
n = 6
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"6! = {factorial}") # 720
'''

# task 8
# Вычисление суммы факториалов
# s = 1! + 2! + ... + 6!
'''
s = 0
factorial = 1
for n in range(1, 7):
    factorial *= n
    s += factorial

print(s) # 873
'''

# task 9
'''
s = 0
factorial = 1
sign = -1

for n in range(1, 7):
    factorial *= n

    part = (sign ** n) * (5 ** n) / factorial
    s += part

print(s) # 8.368055555555557
'''

# task 10
# Возведение 3**7 без исп. **
'''
base = 3
result = 1

for _ in range(7):
    result *= base

print(result) # 2187
'''

# task 11
'''
# a)
for i in range(1, 7):
    print(i, end=" ")
print()
# б)
for _ in range(6):
    print(5, end=" ")
'''

# task 12
'''
x = float(input("Введите x: "))
s = 1

for n in range(1, 11):
    s += 1 / (x ** n)

print(s) # при x = 3 ответ: 1.499991532456096
'''

# task 13
'''
x = -1.5
h = 0.1

print("x    |    y")
print("-----------")

# почему +0.1 необходим для вывода x = 1.5?
while x <= 1.5+0.1:
    if x <= -1:
        y = 1
    elif -1 < x <= 1:
        y = -x
    else:
        y = -1
    
    # Форматированный вывод. 1 знак после запятой для x и 2 знака для y
    print(f"{x:.1f}   {y:.2f}")
    
    x += h
'''

# task 14
'''
fib1 = 1
fib2 = 1

# Вычисляем и печатаем члены Фибоначи
print(fib1, fib2, end=" ")
for _ in range(6):
    next_fib = fib1 + fib2
    print(next_fib, end=" ")
    fib1 = fib2
    fib2 = next_fib

# 1 1 2 3 5 8 13 21
'''

# task 15
'''
# Инициализация числителей и знаменателей
num1, den1 = 1, 1
num2, den2 = 2, 1

# Вычисляем следующие три дроби до пятого члена
for _ in range(3):
    num_next = num1 + num2
    den_next = den1 + den2
    
    num1, den1 = num2, den2
    num2, den2 = num_next, den_next

print(f"5-й член последовательности: {num2}/{den2}")
'''
