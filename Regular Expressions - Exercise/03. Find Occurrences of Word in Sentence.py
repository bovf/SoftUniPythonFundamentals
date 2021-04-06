import re

text = input()

pattern = "\\b" + input() + "\\b"
matches = re.findall(pattern, text, re.IGNORECASE)

print(len(matches))
