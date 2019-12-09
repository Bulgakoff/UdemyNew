class Animal:
    def __init__(self):
        self.health = 100


    def hit(self, damage):
        self.health -= damage
        return self.health


class Carnivor(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 4


print('//////////////////////////')
c = Carnivor()
c.hit(20)
print(f'--------------{c.health}')