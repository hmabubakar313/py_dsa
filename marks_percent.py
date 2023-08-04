student_list = [
    {'name': 'alpha', 'marks': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
    {'name': 'beta', 'marks': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
    {'name': 'gamma', 'marks': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]}
]

student_name = input('Enter student name: ')
for student in student_list:
    if student['name'] == student_name:
        student['marks'].sort()
        print(student['marks'])
        average = sum(student['marks'])/len(student['marks'])
    
print(f'Average marks of {student_name} is {average}')