import re

number_pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"

telephone_numbers = input()
valid_numbers = re.findall(number_pattern, telephone_numbers)

print(", ".join(valid_numbers))
