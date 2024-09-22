# Task 1
'''
import math
# Входные данные
x = float(input("Введите значение x: "))
epsilon = 0.0001
s = 0
n = 1

# Цикл для вычисления суммы
while True:
    part = math.cos(n * x) / (n ** 2)  # очередной член
    s += part  # добавляем член к сумме
    
    if abs(part) < epsilon: # модуль члена меньше epsilon ?
        break  
    
    n += 1

print(f"Значение суммы: {s}") # при x = 10 Ответ = -0.7395947625119912
'''

# Task 2
'''
L = 30_000
product = 1 # произведение. Оно же p
step = 3
n = 1 # поиск макс. n

while product <= L:
    product *= n  # Домножаем произведение
    n += step

# Откатываемся к предыдущему шагу
n -= step

print(f"Наибольший сомножитель n = {n}") # 16
'''

# Task 3
'''
# Входные данные
a = float(input("Первый член прогрессии a = "))
h = float(input("Шаг прогрессии h = "))
p = float(input("Заданное число p = "))
S = 0
n = 0

while S <= p:
    S += (a + n * h)  # Добавляем очередной член в сумму
    n += 1

# Результат
n -= 1  # Откат к наибольшему числу n, при которых условие S <= p выполняется
print(n)
'''

# Task 4
'''
print("Введите значение x (|x| < 1): ")
x = float(input())
epsilon = 0.0001
S = 1  # начальная сумма (1 + ...)
n = 1
part = x ** 2  # первый член x^2

while part >= epsilon:
    S += part
    n += 1
    part = x ** (2 * n)  # следующий член x^(2n)

print(S) # Итоговая сумма при х = 0.4 будет 1.1904562176000004
'''

# Task 5
'''
# Входные данные
N = int(input("Введите число N: "))
M = int(input("Введите число M: "))
quotient = 0 # Частное

while N >= M:
    N -= M # Уменьшение делимого (формирование остатка)
    quotient += 1 # Увеличение частного (сколько раз удалось поделить)

print(f"Частное: {quotient}, Остаток: {N}")
'''

# Task 6 -- Не понял, о какой задаче 18 уровня идёт речь.
# Сказано пропустить этот номер

# Task 7
'''
'''
initial_distance = 10  # начальная дистанция = 10 км
increase_rate = 0.1  # увеличение дневной нормы на 10%

# a) Суммарный путь за 7 дней
distance = initial_distance
total = 0
for day in range(7): # 7 дней
    total += distance
    distance += distance * increase_rate
print("Суммарный путь за 7 дней = ")
print(total) # 

# б) Количество дней, для преодоления 100 км
distance = initial_distance
total = 0
days = 0
while total < 100: # 100 км
    total += distance
    distance += distance * increase_rate
    days += 1

print("Количество дней, чтобы пробежать 100 км = ")
print(days)

# c) Через сколько дней спортсмен будет пробегать в день больше 20 км
distance = initial_distance
days = 0

while distance <= 20: # Больше 20 км или нет?
    distance += distance * increase_rate
    days += 1
days + 1  # TODO: Добавляем 1, так как считаем полный день

print("Количество дней до пробежки более 20 км в день = ")
print(days)


# Task 8
'''
initial_amount = 10_000
interest = 0.08  # Ежемесячный процент
goal = initial_amount * 2 # Целевая сумма
months = 0 # Прошедших месяцев
current_amount = initial_amount # Текущая сумма

# Расчет количества месяцев до удвоения суммы
while current_amount < goal:
    current_amount += current_amount * interest
    months += 1

print(f"Сумма удвоится через {months} месяцев.") # 10 месяцев
'''

