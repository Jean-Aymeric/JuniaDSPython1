from Person import Person
from Building import Building


class House(Building):
    __persons: [Person]

    def __int__(self, name: str):
        Building.__init__(self, name)
        self.__persons = []

    def addPerson(self, person: Person):
        self.__persons.append(person)
