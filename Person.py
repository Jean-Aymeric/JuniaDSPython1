from Factory import Factory
from House import House


class Person:
    __gender: str
    __firstName: str
    __lastName: str
    __house: House
    __factory: Factory

    def __int__(self, gender: str, firstName: str, lastName: str):
        self.__gender = gender
        self.__firstName = firstName
        self.__lastName = lastName
        self.__house = None
        self.__factory = None

    def getGender(self) -> str:
        return self.__gender

    def getFirstName(self) -> str:
        return self.__firstName

    def getLastName(self) -> str:
        return self.__lastName

    def getFactory(self) -> Factory:
        return self.__factory

    def liveIn(self, house: House):
        self.__house = house
        house.addPerson(self)

    def workIn(self, factory: Factory):
        self.__factory = factory
