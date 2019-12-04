num = [1, 2, 3, 4]
print(type(num))


class Character():
    def __init__(self, race, damage=10, armor=20):# damage=10, armor=20 сустановка по умолчанию
        self.race = race
        self.damage = damage
        self.armor = armor



unit = Character('Elf', 50, 100)# для damage=10, и  armor=20

print(type(unit))
print(unit.race)
print(unit.damage)
print(unit.armor)

