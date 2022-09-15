# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
used = []
for st in students:
    if st in used:
        pass
    else:
        print(f'{st["first_name"]}: {students.count(st)}')
        used.append(st)

# ???


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
name_count = students.count(0)
name = students[0]['first_name']
for st in students:
    if students.count(st) > name_count:
        name_count = students.count(st)
        name = st['first_name']
print(f'Самое частое имя среди учеников: {name}')
# ???


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
def classname(dict):
    name_count = dict.count(0)
    name = dict[0]['first_name']
    for di in dict:
        if dict.count(di) > name_count:
            name_count = dict.count(di)
            return di['first_name']
for st in enumerate(school_students):
    print(f'Самое частое имя в классе {st[0]+1}: {classname(st[1])}')
# ???


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for sch in school:
    girls = 0
    boys = 0
    for stu in sch['students']:
        if is_male[stu['first_name']] is False:
            girls +=1
        else:
            boys +=1
    print(f'Класс {sch["class"]}: девочки {girls}, мальчики {boys}')




# ???


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

boy_class_num = 0
girls_class_num = 0

for sc in school:
    girls = 0
    boys = 0
    for stu in sc["students"]:
        if is_male[stu['first_name']] is False:
            girls +=1
        else:
            boys +=1
        if girls > girls_class_num:
            girls_class_num = girls
            girls_class = sc["class"]
        if boys > boy_class_num:
            boy_class_num = boys
            boy_class = sc["class"]
print(f'Больше всего мальчиков в классе {boy_class}')
print(f'Больше всего девочек в классе {girls_class}')
# ???

