import re

text = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

for match in matches:
    print(f"{match.group(0)}", end=" ")
