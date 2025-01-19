person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(person)
print(name, last_name, city, phone, country)


a = 'результат операции: 42'
b = 'результат операции: 514'
c = 'результат работы программы: 9'
print(int((a[(a.index('42')):])) + 10)
print(int((b[(b.index('514')):])) + 10)
print(int((c[(c.index('9')):])) + 10)


students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students1 = ', ' .join(students)
subjects1 = ', ' .join(subjects)
print(students1)
print(subjects1)
print('Students', students1, 'study these subjects:', subjects1)
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
print(f'Students {students1} study these subjects: {subjects1}')
