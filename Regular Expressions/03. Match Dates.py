import re

pattern = "(?P<day>\\d{2})(?P<separator>[\\.\\-\\/])(?P<month>[A-Z]{1}[a-z]{2})(?P=separator)(?P<year>[1-9][0-9]{3})"

text = input()
matches = re.finditer(pattern, text)

for match in matches:
    print(f"Day: {match.group('day')}, Month: {match.group('month')}, Year: {match.group('year')}")
