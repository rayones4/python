student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77, 'Akshay':80, 'Soyuj': 72, 'Sam':55}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with tha name found.')