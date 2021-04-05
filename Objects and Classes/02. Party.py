class Party:
    def __init__(self):
        self.people = []

    def add_to_party(self, name):
        self.people.append(name)

    def get_number_of_people(self):
        return len(self.people)

    def get_people(self):
        return ", ".join(self.people)


party = Party()

while True:
    command = input()

    if command == "End":
        break

    party.add_to_party(command)

print(f"Going: {party.get_people()}")
print(f"Total: {party.get_number_of_people()}")
