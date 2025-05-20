#sampleClass.py
class PartyAnimal:
    def __init__(self):
        self.x = 0

    def Party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.Party()
an.Party()
an.Party()


#lifecycle.py
#2-1
class PartyAnimal:
    def __init__(self):
        self.x = 0
        print('I am constructed')

    def Party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def __del__(self):
        print('I am constructed', self.x)

an = PartyAnimal()
an.Party()
an.Party()
an = 42
print('an contains', an)

#2-2
    def __init__(self, z):
        self.x = 0
        self.name = z
        print(self.name, "constructed")

    def Party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("Sally")
s.Party()
j = PartyAnimal("Jim")

j.Party()
s.Party()

#inheritance.py
class PartyAnimal:

    def __init__(self, nam):
        self.x = 0
        self.name = nam
        print(self.name, "constructed")

    def Party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)


class FootballFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.Party()
        print(self.name, "points", self.points)

s= PartyAnimal("Sally")
s.Party()

j = FootballFan("Jim")
j.Party()
j.touchdown()