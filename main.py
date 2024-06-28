
#Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать
# вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
result = dict(zip(sorted(students), map(lambda x: sum(x) / len(x), grades)))

# Выводим результат
print(result)


# Второй вариант решения
# result = {}
# for i, student in enumerate(students):
#     grades_sum = sum(grades[i])
#     grades_len = len(grades[i])
#     avg_grade = grades_sum / grades_len
#     result[student] = avg_grade
#
# print(result)