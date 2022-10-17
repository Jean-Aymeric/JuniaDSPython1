from Building import Building
from Company import Company


class Factory(Building):
    __company: Company

    def __init__(self, name: str):
        Building.__init__(self, name)
        self.__company = None

    def setCompany(self, company: Company):
        self.__company = company
