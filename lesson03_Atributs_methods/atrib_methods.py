class Animal():
    max_size = 100  # СТАТИЧНЫЙ АТРИБУТ более глобальное свойство может
    # относиться ко всем экземплярам, вызывается напрямую от класса
    deaf_health = 0

    def __init__(self, breed, damage, name='Sher', age=10):  # создание атрибутов извне  constructor инстанции
        self.breed = breed  # порода -ДИНАМИЧНЫЙ атрибут инстации
        self.damage = damage
        self.age = age
        self.name = name
        self.self_health = 101  # создание атрибутов изнутри, тоже получается СТАТИЧНЫЙ АТРИБУТ  глобальный

    def hit(self, damage):
        self.self_health = self.self_health - damage
        return self.self_health

    def is_death(self):
        return self.self_health == Animal.deaf_health

    # def __init__(self, name):  # constructor инстанции ДВУХ КОНСТРУКТОРОВ НЕ МОЖЕТ БЫТЬ
    #     self.name = name


print('# СТОРОНА КЛИЕНТА/////////////////////////////////////')
unit1 = Animal('pantera', 50, 'Bagira', 20)  # клиент
unit2 = Animal('tiger', 40, 'sher', 5)
unit1.self_health = 250  # можно на прямую воздействоать на атрибуты экземпляра
# (а как же инкапсуляция )
unit1.hit(20)
res = unit1.is_death()
print(f'--remain --> {unit1.self_health} lifes')
print(f'----> умер ли перснаж --- {res} ')
unit1.hit(81)
res = unit1.is_death()
print(f'--remain --> {unit1.self_health} lifes')
print(f'----> умер ли перснаж --- {res} ')

print(Animal.max_size)  # более глобальное свойство может
# относиться ко всем экземплярам, вызывается напрямую от класса

print(unit1.name)
print(unit1.age)
print(unit1.self_health)
print('//////////////')
print(unit2.name)
print(unit2.age)
print(unit2.self_health)
