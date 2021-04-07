import re


regex_patter = r">>(?P<item>[A-Za-z]+)<<(?P<price>[0-9]+|[0-9]+\.[0-9]+)!(?P<quantity>[0-9]+)"

items = []
money_spent = 0

while True:
    text = input()
    if text == "Purchase":
        break

    matches = re.finditer(regex_patter, text)
    for match in matches:
        item = match.group("item")
        cost = float(match.group("price"))
        quantity = int(match.group("quantity"))
        items.append(item)
        money_spent += cost * quantity


print(f"Bought furniture:")
for item in items:
    print(item)
print(f"Total money spend: {money_spent:.2f}")
