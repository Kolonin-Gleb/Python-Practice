# Мой вариант N = 8
# Поэтому мне нужно решить номера:
# 8 % 3 = 2
# Начиная со 2ого с шагом 3
# (2, 5, 8, 11, 14, ... при наличии)

################################## LEVEL 1

# Task 2
# Пример решения в GeoGebra: https://www.geogebra.org/m/gark3ugr
'''
# Дан треугольник с вершинами в точках (-1; 0), (1; 0), (0; 1)
# Определить лежит ли заданная точка внутри треугольника.
# => точку нужно задать.
# Из указания следует: Точка принадлежит фигуре, если (y >= 0) и (y + |x| <= 1)

def is_point_in_triangle(x, y):
    condition1 = y >= 0  # Точка должна быть выше оси X
    # Два случая раскрытия модуля и сравнения с y
    condition2 = y <= 1 + x  # Линия слева: y = 1 + x  (при x < 0)
    condition3 = y <= 1 - x  # Линия справа: y = 1 - x (при х > 0)
    
    # Если все условия выполняются, точка внутри треугольника
    return condition1 and condition2 and condition3

# Пример координат точек для проверки
points = [(0, 2), (0.5, 0.7), (1, 1), (0.2, 0.3)]

for (x, y) in points:
    if is_point_in_triangle(x, y):
        print(f"Точка ({x}, {y}) лежит внутри треугольника.")
    else:
        print(f"Точка ({x}, {y}) лежит вне треугольника.")
'''

# Task 5
# Пример решения в GeoGebra: https://www.geogebra.org/m/tjwbuwjs
# Определить поместится ли квадрат площади s в круг радиуса r
'''
def is_square_fits_in_circle(r, s):
    a = s**0.5 # Сторона квадрата
    diag = a * 2**0.5 # Диагональ квадрата
    diameter = 2 * r # Диаметр круга
    print(diameter)
    # Помещается ли квадрат в круг
    return (diag <= diameter)

# Заданные параметры
# 1) 
r1 = 70
s1 = 36.74
# 2) 
r2 = 0.86
s2 = 0.74
# Результаты
print("Для r = 70 и s = 36.74 квадрат помещается в круге:", is_square_fits_in_circle(r1, s1))
print("Для r = 0.86 и s = 0.74 квадрат помещается в круге:", is_square_fits_in_circle(r2, s2))
'''

# Task 8
'''
def function_y(x):
    if abs(x) >= 1:
        y = 0
    else:
        y = x ** 2 - 1
    return y

x_values = [1.5, -2, 0.5, -0.2, 0, 1]
for x in x_values:
    y = function_y(x)
    print(f"Для x = {x}, y = {y}")
'''


################################## LEVEL 2 and LEVEL 3
# Уровень 3 = Дополнить задачи из LEVEL 2 вводом данных до момента,
# когда пользователь решит остановиться.

# Task 2 (level 3 done)
'''
# Функция для проверки, лежит ли точка внутри круга
def is_point_in_circle(x, y, a, b, r):
    # Расстояние от точки до центра круга
    distance = ((x - a) ** 2 + (y - b) ** 2) ** 0.5

    # Если расстояние меньше или равно радиусу, точка лежит внутри круга
    return distance <= r

# Входные данные
a = float(input("Введите координату a (x центра круга): "))
b = float(input("Введите координату b (y центра круга): "))
r = float(input("Введите радиус круга r: "))
# n = int(input("Введите количество точек: "))

# Инициализация счетчика
inside_circle = 0

# Ввод координат n точек
# for i in range(n):
exit = 0
while exit != 1:
    # print(f"Ввод координат точки {i+1}")
    print("Ввод координат точки")
    x = float(input(f"Введите координату x для точки: "))
    y = float(input(f"Введите координату y для точки: "))
    # Проверяем, попадает ли точка в круг
    if is_point_in_circle(x, y, a, b, r):
        # print(f"Точка ({x}, {y}) лежит внутри круга.")
        inside_circle += 1
    # else:
        # print(f"Точка ({x}, {y}) лежит вне круга.")
    exit = int(input("Введите 1 для прекращения ввода и 0 для продлолжения: "))


# Сколько точек попало в круг с радиусом r с центром в точке (a; b)
print(f"Количество точек, попавших в круг: {inside_circle}")
'''

# Task 5 (level 3 done)
'''
standard = 60 # Пусть норматив - пробежать за 60 секунд
passed = 0 # Прошедших норматив

print("Введите результаты спортсменов: ")
# for i in range(30):
exit = 0
while exit != 1:
    # result = float(input(f"Спортсмен {i + 1} пробежал за секунд = "))
    result = float(input(f"Спортсмен пробежал за секунд = "))
    if result <= standard:
        passed += 1
    exit = int(input("Введите 1 для прекращения ввода и 0 для продлолжения: "))

print(f"Количество спортсменов, выполнивших норматив: {passed}")
'''

# Task 8 (level 3 done)
'''
def get_closest_point_data(points):
    closest_point_index = None
    min_distance = float('inf')  # начальное значение бесконечность

    for i, (x, y) in enumerate(points):
        distance = (x**2 + y**2) ** 0.5 # вычисляем расстояние до начала координат
        
        if distance < min_distance:
            min_distance = distance
            closest_point_index = i  # сохраняем индекс точки

    return closest_point_index, min_distance


# n = int(input("Введите количество точек: "))
n = 0

points = []
# for i in range(n):
exit = 0
while exit != 1:
    # x = float(input(f"Введите координату x для точки {i+1}: "))
    x = float(input(f"Введите координату x для точки: "))
    # y = float(input(f"Введите координату y для точки {i+1}: "))
    y = float(input(f"Введите координату y для точки: "))
    points.append((x, y)) # Сохранение данных точки в виде кортежа в список

    exit = int(input("Введите 1 для прекращения ввода и 0 для продлолжения: "))

# Поиск и получение данных ближайшей точки
index, distance = get_closest_point_data(points)

# Вывод результата
print(f"Точка под номером {index + 1} является ближайшей к началу координат.")
print(f"Расстояние до начала координат: {distance:.2f}")
'''

# Task 11 (level 3)
'''
# Получение данных группы
# (Кол. неуспевающих и средний балл)
def get_group_data(students):
    failing_students = 0
    grades_sum = 0 # Сумма оценок студентов группы
    for grades in students:
        student_avg_grade = sum(grades) / 4 # / 4 Ведь у каждого 4 оценки
        # Студентов с средним баллом < 3, считаем неуспевающими
        if student_avg_grade < 3:
            failing_students += 1
        grades_sum += sum(grades)

    # Средний балл группы = все оценки делить на их количество
    group_avg = grades_sum / (len(students)*4)
    return failing_students, group_avg


# n = int(input("Введите количество студентов: "))

# Ввод оценок студентов
students = []
exit = 0
# for i in range(n):
while exit != 1:
    # print(f"Введите 4 оценки для студента {i+1}:")
    print(f"Введите 4 оценки для студента:")
    grades = []
    for j in range(4):
        grade = float(input(f"Оценка {j+1}: "))
        grades.append(grade)
    students.append(grades)

    exit = int(input("Введите 1 для прекращения ввода и 0 для продлолжения: "))

# Рассчёт неуспевающих студентов
failing_students, group_average = get_group_data(students)

# Вывод результатов
print(f"Число неуспевающих студентов: {failing_students}")
print(f"Средний балл группы: {group_average:.2f}")
'''

