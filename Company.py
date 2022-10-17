from Factory import Factory


class Company:
    __name: str
    __factories: [Factory]

    def __int__(self, name: str):
        self.__name = name
        self.__factories = []

    def getName(self) -> str:
        return self.__name

    def addFactory(self, factory: Factory):
        self.__factories.append(factory)
