class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        join_str = ", "
        result = ""
        if species == "mammal":
            result = f"Mammals in {self.name}: {join_str.join(self.mammals)}\n"
        elif species == "fish":
            result = f"Fishes in {self.name}: {join_str.join(self.fish)}\n"
        elif species == "bird":
            result = f"Birds in {self.name}: {join_str.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo = Zoo(input())
animals_total = int(input())

for _ in range(animals_total):
    command_list = input().split()
    zoo.add_animal(command_list[0], command_list[1])

print(zoo.get_info(input()))


