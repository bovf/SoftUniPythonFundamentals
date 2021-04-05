import sys

number_of_electrons = int(input())

electrons_left = number_of_electrons
electron_shell = 0
electron_shells_list = []

for electron_shell_number in range(1, sys.maxsize):
    if electrons_left == 0:
        break
    else:
        while not electron_shell == 2 * (electron_shell_number ** 2):
            electron_shell += 1
            electrons_left -= 1
            if electrons_left == 0:
                break
        electron_shells_list.append(electron_shell)
        electron_shell = 0

print(electron_shells_list)
