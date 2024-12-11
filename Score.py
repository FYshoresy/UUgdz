grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_score = {student: grade for student, grade in zip(students, grades)}
average_score = {}
for student, grades in students_score.items(): average_score[student] = sum(grades) / len(grades)
print (average_score)