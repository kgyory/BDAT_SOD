import abc
from typing import List


class Ente(abc.ABC):
    def __init__(self, name: str, gewicht: int):
        self._name = name
        self._gewicht = gewicht

    @property
    def gewicht(self):
        return self._gewicht

    @property
    def name(self):
        return self._name

    @abc.abstractmethod
    def get_full_weight(self) -> int:
        pass

    @abc.abstractmethod
    def make_noise(self) -> str:
        pass


class FlugEnte(Ente):
    def __init__(self, name: str, gewicht: int, gewicht_federn: int):
        super().__init__(name, gewicht)
        self.gewicht_federn = gewicht_federn

    def get_full_weight(self) -> int:
        full_weight = self._gewicht + self.gewicht_federn
        return full_weight

    def make_noise(self) -> str:
        return f'{self._name} sagt Quack'

    def __repr__(self):
        return f'Flugente {self._name}'


class BadeEnte(Ente):
    def __init__(self, name: str, gewicht: int, gewicht_wasser: int):
        super().__init__(name, gewicht)
        self.gewicht_wasser = gewicht_wasser

    def get_full_weight(self) -> int:
        full_weight = self._gewicht + self.gewicht_wasser
        return full_weight

    def make_noise(self) -> str:
        return f'{self._name} sagt Quietsch'

    def __repr__(self):
        return f'Badeente {self._name}'


class EntenHausen:
    def __init__(self):
        self.__enteliste = []

    def add_ente(self, ente: Ente):
        self.__enteliste.append(ente)

    def get_gruppierte_enten(self) -> [int, List[Ente]]:
        grp1 = []
        grp2 = []
        grp3 = []
        entengruppierung = {100: None, 200: None, 300: None}
        y = 0
        for x in self.__enteliste:
            if x.get_full_weight() <= 100:
                grp1.append(self.__enteliste[y])
            elif x.get_full_weight() <= 200:
                grp2.append(self.__enteliste[y])
            elif x.get_full_weight() <= 300:
                grp3.append(self.__enteliste[y])
            y += 1
        entengruppierung.update([(100, grp1), (200, grp2), (300, grp3)])
        return entengruppierung

        # ausgangsdict erstellen, mit ints und none?
        # die leere listen auch erstellen
        # object von der Liste mit for auslesen
        # gewicht von den obj definieren -> var
        # mit if die gewicht einstufen und in die listen einfügen
        # die dict aktualisieren


if __name__ == '__main__':
    a = FlugEnte('Donald', 80, 10)
    print(a.get_full_weight())
    print(a.make_noise())

    b = BadeEnte('Peter', 150, 50)
    print(b.get_full_weight())
    print(b.make_noise())

    c = BadeEnte('Thomas', 220, 30)
    print(c.get_full_weight())
    print(c.make_noise())

    d = FlugEnte('Alex', 70, 15)

    e = EntenHausen()
    e.add_ente(a)
    e.add_ente(b)
    e.add_ente(c)
    e.add_ente(d)

    print(e.get_gruppierte_enten())