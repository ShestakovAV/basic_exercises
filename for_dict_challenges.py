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
def calculation(students):
    students_list = {}
    for student in students:
        if student['first_name'] in students_list:
            students_list[student['first_name']] += 1
        else:
            students_list[student['first_name']] = 1
    return students_list
students_list_1 = calculation(students)
for name in students_list_1:
    print(f'{name}: {students_list_1[name]}')
    


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
def most_popular_name(students):
    students_list_2 = calculation(students)
    amount = 0
    most_popular = ''
    for name in students_list_2:
        if students_list_2[name] > amount:
            most_popular = name
            amount = students_list_2[name]
    return most_popular
name = most_popular_name(students)
print(f'Cамое частое имя среди учеников: {name}')

    


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
for number, students in enumerate(school_students, start=1):
    name = most_popular_name(students)
    print(f'Cамое частое имя в классе {number}: {name}')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def students_count(school, is_male):
    school_list = []
    for classes in school: #распаковка списка словарей(классов)
        male_dict = {}
        male_dict['class'] = classes['class']
        #print(male_dict['class'])
        students = classes['students']
        male = 0
        female = 0
        for student in students:            #распаковка списка словарей(студентов) и подсчет мальчиков и девочек
            student_name = student['first_name']
            #print(students)
            if is_male[student_name] == True:
                male += 1
            else:
                female +=1
            #print(male,female)
            male_dict['boys'] = male
            male_dict['girls'] = female
        #print(male_dict['boys'],male_dict['girls'])
        school_list.append(male_dict)
        #print(school_list)
    return school_list
list_for_print = students_count(school, is_male)
for element in list_for_print:
    print(f'Класс {element["class"]}: девочки {element["girls"]}, мальчики {element["boys"]}')

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
# ???
students_in_classes = students_count(school, is_male)
max_boys = students_in_classes[0]
max_girls = students_in_classes[0]
for clas in students_in_classes:
    if clas['boys'] > max_boys['boys']:
        max_boys = clas
    if clas['girls'] > max_girls['girls']:
        max_girls = clas
print(f'Больше всего маьчиков в классе {max_boys["class"]}')
print(f'Больше всего девочек в классе {max_girls["class"]}')
#max_boys = max(students_in_classes['boys'])
#print(max_boys)
