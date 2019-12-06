class Charac():
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.__race = race  # приватный __
        self.damage = damage
        self._health = 1000  # _ защищенный
        self._current_speed = 20

    def hit(self, dama):
        self._health -= dama
        return self._health

    @property       #это свойство только на чтение
    def health(self):
        return self._health

    @property    #это свойство только на чтение
    def race(self):
        return self.__race

    @property #-----------------> это свойство только на чтение
    def current_speed(self):#  это гетер?????????????????
        return self._current_speed

    @current_speed.setter#а это связанный с ним сеттер ?????? это свойство с возможностью изменений
    def current_speed(self, c_s):
        if c_s < 0:
            print(f'you lowered speed {self._current_speed} will be set up 0 ')
            self._current_speed = 0
        elif c_s > 100:
            print('you overed speed ')
            self._current_speed = 100
        else:
            self._current_speed = c_s


print(Charac.MAX_SPEED)

Charac.MAX_SPEED = 10
print(Charac.MAX_SPEED)

c = Charac('Elf')
c._Charac__race = 'Ork'  # но доступ к атрибуту возможен со внесением изиенеий
print(c._Charac__race)  # Ork

print(c.hit(400))

c._health = 0  # обращение к защищеннойму атрибуту
print(c._health)
print()
print(f'----------------------------->{c.health}')
print(c.race) #это свойство только на чтение

print(f'----------просто читаем---------------------->{c.current_speed}')

c.current_speed = -10000

print(f'--------после измениний---------->{c.current_speed}')
