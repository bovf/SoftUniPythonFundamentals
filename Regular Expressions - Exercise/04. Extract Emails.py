import re

text = input()
pattern = r"(?<=\s)((?P<username>[a-zA-Z0-9]+)(?P<separator>[\.\-\_]?))+\@(?P<domain>\w+[\-\w+]*)(?P<com>(\.\w+)+)"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(0))
