import re

names = input()
regex_pattern = "\\b[A-Z][a-z]+ \\b[A-Z][a-z]+\\b"
matches = " ".join(re.findall(regex_pattern, names))
print(matches)
