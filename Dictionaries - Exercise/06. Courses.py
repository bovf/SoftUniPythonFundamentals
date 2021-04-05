courses = {}

while True:
    command = input()
    if command == "end":
        break
    else:
        command = command.split(" : ")
        course_name = command[0]
        course_participant = command[1]

    if course_name not in courses.keys():
        courses[course_name] = [course_participant]
    else:
        courses[course_name].append(course_participant)

courses = {k: v for k, v in sorted(courses.items(), key=lambda item: len(item[1]), reverse=True)}

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    courses[course] = [el for el in sorted(courses[course], key=lambda item: item, reverse=False)]
    for participant in courses[course]:
        print(f"-- {participant}")
