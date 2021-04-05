companies = {}

while True:
    command = input()
    if command == "End":
        break
    else:
        command = command.split(" -> ")
        company = command[0]
        user = command[1]

    if company not in companies:
        companies[company] = [user]
    else:
        if user not in companies[company]:
            companies[company].append(user)
        else:
            pass

companies = {k: v for k, v in sorted(companies.items(), key=lambda item: item[0], reverse=False)}

for company in companies.keys():
    print(f"{company}")
    for user in companies[company]:
        print(f"-- {user}")
