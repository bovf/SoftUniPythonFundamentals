current_year = int(input())


def happy_year_checker(a):
    year_bool = bool
    for i in range(len(str(a))):
        for e in range(i + 1, (len(str(a)))):
            if str(a)[i] != str(a)[e]:
                year_bool = True
            else:
                year_bool = False
                return year_bool
    return year_bool


is_it_a_happy_year = happy_year_checker(current_year)
if is_it_a_happy_year:
    current_year += 1
    is_it_a_happy_year = happy_year_checker(current_year)

while not is_it_a_happy_year:
    current_year += 1
    is_it_a_happy_year = happy_year_checker(current_year)

print(current_year)
