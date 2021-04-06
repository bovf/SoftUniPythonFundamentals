import re

text = input()
pattern = r"\d+"

all_valid_numbers = ""
while text:

    matches = re.findall(pattern, text)
    if not matches == []:
        all_valid_numbers += ' '.join(matches) + " "
    text = input()

print(f"{all_valid_numbers}")
