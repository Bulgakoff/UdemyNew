class Animal:
    def die(self):
        print('bye-bye')
        self.health = 0


class Carnivor:
    def hunt(self):
        print('eating and hunting')
        self.satiety = 100


class Dog(Animal, Carnivor):
    def bark(self):
        print('woof-woof')


print('////////////////////////////////////')

dog = Dog()
print(f'==============>{dog.bark()}--{dog.hunt()}--{dog.die()}-')
