employee_happiness = input(). split(" ")
happiness_improvement_factor = int(input())

employee_happiness_total = list(map(lambda x: int(x) * happiness_improvement_factor, employee_happiness))
average_happiness = sum(employee_happiness_total) / len(employee_happiness_total)

happy_employees = [happiness for happiness in employee_happiness_total if happiness > average_happiness]


def are_employees_happy(employees, employees_happy):
    number_employees = len(employees)
    employees_happy = len(employees_happy)

    if employees_happy >= number_employees / 2:
        return True
    else:
        return False


if are_employees_happy(employee_happiness_total, happy_employees):
    print(f"Score: {len(happy_employees)}/{len(employee_happiness_total)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(employee_happiness_total)}. Employees are not happy!")
