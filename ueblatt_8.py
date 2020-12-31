import abc
from typing import Dict


class RealEstate(abc.ABC):
    def __init__(self, square_meter: float):
        self.square_meter = square_meter
        
    @property
    def square_meter(self):
        return self.__square_meter
    
    @square_meter.setter
    def square_meter(self, value):
        self.__square_meter = value

    @abc.abstractmethod
    def calc_lease(self) ->float:
        pass

    @property
    def category(self) -> float:
        return self.__square_meter / 10

    def __repr__(self):
        return f'RealEstate'

class Office(RealEstate):
    def __init__(self, square_meter: float, people: int):
        super().__init__(square_meter)
        self.__people = people

    def calc_lease(self) ->float:
        if self.__people >= 100:
            lease = self.square_meter * 8.5 + self.__people
        elif self.__people >= 50:
            lease = self.square_meter * 8.2 + 90
        else:
            lease = self.square_meter * 8
        return lease

    def __repr__(self):
        return f'Office, size: {self.square_meter}, persons: {self.__people}'


class Flat(RealEstate):
    def __init__(self, square_meter: float, count_room: int, typ: str):
        super().__init__(square_meter)
        self.__count_room = count_room
        self.__typ = typ

    def calc_lease(self) ->float:
        if self.__typ == "Low":
            lease = self.square_meter * 7
        elif self.__typ == "Standard":
            lease = (self.square_meter * 7.5) + (self.__count_room * 10)
        elif self.__typ == "High":
            lease = (self.square_meter * 8 ) + (self.__count_room * 12 )
        else:
            lease = -1
        return lease

    def __repr__(self):
        return f'Flat, size {self.square_meter}, rooms: {self.__count_room}, Type: {self.__typ}'

class House(RealEstate):
    def __init__(self, square_meter: float, garden: bool):
        super().__init__(square_meter)
        self.__garden = garden

    def calc_lease(self) -> float:
        if self.__garden:
            lease = (self.square_meter * 10) + 200
        else:
            lease = self.square_meter * 15
        if lease < 1000:
            lease = 1000
        return lease

    def __repr__(self):
        if self.__garden:
            a = "with graden"
        else:
            a = "without graden"
        return f'House {a}, size: {self.square_meter}'

class Accounting:
    def __init__(self):
        self.__real_estates = []

    def add(self, re: RealEstate):
        self.__real_estates.append(re)

    def print_all(self):
        for x in self.__real_estates:
            print (x, "Lease: ",x.calc_lease())

    def get_overall_lease(self) -> float:
        y = 0
        for x in self.__real_estates:
            y += x.calc_lease()
        return y

    def get_average_lease(self) -> float:
        y = 0
        for x in self.__real_estates:
            y += x.calc_lease()
        return y / len(self.__real_estates)

    def get_real_estate_in_category(self) -> Dict[int, int]:
        category_dict = {}
        for x in self.__real_estates:
            if x.category in category_dict:
                category_dict[x] += 1
            else:
                category_dict[x.category] = 1
        return category_dict

if __name__ == '__main__':
    office = Office(500, 36)
    flat = Flat(90, 4, "High")
    house = House(150, True)

    print(office.calc_lease())
    print(flat.calc_lease())
    print(house.calc_lease())

    print(office.category)

    acc = Accounting()

    acc.add(office)
    acc.add(flat)
    acc.add(house)

    acc.print_all()
    print(acc.get_overall_lease())
    print(acc.get_average_lease())
    print(acc.get_real_estate_in_category())