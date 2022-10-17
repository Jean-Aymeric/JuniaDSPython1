from Person import Person
from House import House
from Factory import Factory
from Company import Company


p1 = Person("Mme", "Christa", "PAFFGEN")
p2 = Person("M.", "Lou", "REED")
p3 = Person("M.", "Andy", "WHARHOL")

h1 = House("Château")
h2 = House("T3")

p1.liveIn(h1)
p2.liveIn(h2)

f1 = Factory("The Factory")
c1 = Company("Junia")

p2.workIn(f1)
p3.workIn(f1)

c1.addFactory(f1)
