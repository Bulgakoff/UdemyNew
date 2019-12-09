class Animal:
    def set_health(self, health):
        print('set in Animal')


class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)# что бы не было двоцной инициализации базовых классов super().
        print('set in Carnivour')


class Mammal(Animal):
    def set_health(self, health):
        super().set_health(health)# что бы не было двоцной инициализации базовых классов super().
        print('set in Mammal')


class Dog(Carnivour, Mammal):
    def set_health(self, health):
        super().set_health(health)# что бы не было двоцной инициализации базовых классов super().
        # Carnivour.set_health(self, health)
        # Mammal.set_health(self, health)
        print('set in Dog')


print('///////////////////////////////////////')

dog = Dog()
print(f'-----собака-------{dog.set_health(10)}--')
