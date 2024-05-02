grades = ['5 3 3 5 4', '2 2 2 3', '4 5 5 2', '4 4 3', '5 5 5 4 5']
students = {'Johnni', 'Bilbo', 'Steve', 'Kendrik', 'Aaron'}
grades_dict = {}
# Преобразуем множество в список для индексирования и список в строку
students_list = list(students)
grades_str = str(grades)

# Создаем словарь для хранения средних баллов
average_scores = {}
# Преобразуем grades в список списков целых чисел
grades_list = [list(map(int, grade.split())) for grade in grades]

# Отсортируем множество students в список для соответствия порядка оценок в grades
students_sorted = sorted(students)

# Создадим словарь со средним баллом для каждого ученика

grades_dict = {student: sum(grades_list[i]) / len(grades_list[i]) for i, student in enumerate(students_sorted)}
#Выводим
print(grades_dict)
