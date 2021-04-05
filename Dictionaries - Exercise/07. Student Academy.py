number_of_entries = int(input())
students = {}

for _ in range(number_of_entries):
    student = input()
    grade = float(input())
    if student not in students.keys():
        students[student] = grade
    else:
        students[student] = (grade + students[student]) / 2

passed_students = {k: v for k, v in sorted(students.items(),
                                           key=lambda item: item[1], reverse=True) if v >= 4.5}
for student in passed_students.keys():
    print(f"{student} -> {passed_students[student]:.2f}")
