from random import randint
class Human:
    def __init__(self, name):
        self.name = name
        self.ID = randint(1000, 9999)
    
    def get(self):
        return self.name, self.ID

ism = "xudoyberdi"

ism1 = Human(ism)
print(ism1.get())