import abc
from typing import List, Dict


class Fluessigkeit:
    def __init__(self, name: str, menge: float, alkohol_prozent: float):
        self.name = name
        self.menge = menge
        self.alkohol_prozent = alkohol_prozent


class Brennbar(abc.ABC):
    @abc.abstractmethod
    def brennt(self) -> bool:
        pass


class Getraenk(Brennbar):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f'{self.name}, {self.get_anzahl_zutaten()}, {self.beinhaltet_alkohol()}, {self.brennt()}'

    def brennt(self) -> bool:
        pass

    @abc.abstractmethod
    def get_anzahl_zutaten(self) -> int:
        pass

    @abc.abstractmethod
    def beinhaltet_alkohol(self) -> bool:
        pass

    @abc.abstractmethod
    def menge_in_ml(self) -> float:
        pass


class SimplesGertaenk(Getraenk):
    def __init__(self, name: str, bestandteil: Fluessigkeit):
        super().__init__(name)
        self.bestandteil = bestandteil

    def brennt(self) -> bool:
        return self.bestandteil.alkohol_prozent > 30

    def get_anzahl_zutaten(self) -> int:
        return 1

    def beinhaltet_alkohol(self) -> bool:
        return self.bestandteil.alkohol_prozent > 0

    def menge_in_ml(self) -> float:
        return self.bestandteil.menge


class LongDrink(Getraenk):
    def __init__(self, name: str, spirituose: Fluessigkeit, filler: Fluessigkeit):
        super().__init__(name)
        self.spirituose = spirituose
        self.filler = filler

    def brennt(self) -> bool:
        return self.spirituose.alkohol_prozent > 30

    def get_anzahl_zutaten(self) -> int:
        return 2

    def beinhaltet_alkohol(self) -> bool:
        return self.spirituose.alkohol_prozent > 0

    def menge_in_ml(self) -> float:
        return self.spirituose.menge + self.filler.menge


class Cocktail(Getraenk):
    def __init__(self, name: str, bestandteile: List[Fluessigkeit]):
        super().__init__(name)
        self.bestandteile = bestandteile

    def brennt(self) -> bool:
        y = 0
        for x in self.bestandteile:
            y += x.alkohol_prozent
        return y > 30

    def get_anzahl_zutaten(self) -> int:
        return len(self.bestandteile)

    def beinhaltet_alkohol(self) -> bool:
        y = 0
        for x in self.bestandteile:
            y += x.alkohol_prozent
        return y > 0

    def menge_in_ml(self) -> float:
        y = 0
        for x in self.bestandteile:
            y += x.menge
        return y


class Registrierkasse:
    __verkaufte_getraenke = 0

    def __init__(self):
        self.__getraenkeliste = []

    def verkauft(self, g: Getraenk):
        self.__getraenkeliste.append(g)
        self.__verkaufte_getraenke += 1

    def getraenke_sortiert(self): #Ich habe auch keine Ahnung was Comparator Klasse ist...
        self.__getraenkeliste.sort(key=lambda x: x.get_anzahl_zutaten())
        return self.__getraenkeliste

    def get_g_a_n_z(self) -> Dict[int, List[Getraenk]]:
        g_aufgeteilt = {}
        for z in self.__getraenkeliste:
            y = z.get_anzahl_zutaten()
            if y in g_aufgeteilt:
                g_aufgeteilt[y].append(z.name)
            else:
                g_aufgeteilt[y] = [z.name]
        return g_aufgeteilt


if __name__ == '__main__':
    apfelsaft = Fluessigkeit('apfelsaft', 200, 0)
    cola = Fluessigkeit('cola', 150, 0)
    bier = Fluessigkeit('bier', 500, 5.2)
    vodka = Fluessigkeit('vodka', 5, 40)
    rotwein = Fluessigkeit('rotwein', 150, 12)
    gin = Fluessigkeit('gin', 5, 40)
    eistee = Fluessigkeit('eistee', 100, 0)
    rb = Fluessigkeit('rootbeer', 330, 0)

    apfel_pur = SimplesGertaenk('apfel_pur', apfelsaft)
    gin_otr = SimplesGertaenk('gin_otr', gin)
    # print(gin_otr.brennt())
    # print(gin_otr.get_anzahl_zutaten())
    # print(gin_otr.beinhaltet_alkohol())
    # print(gin_otr.menge_in_ml())

    vc = LongDrink('vodka mit cola', vodka, cola)
    # print(vc.brennt())
    # print(vc.get_anzahl_zutaten())
    # print(vc.beinhaltet_alkohol())
    # print(vc.menge_in_ml())

    vget = Cocktail('vodka gin eistee', [vodka, gin, eistee])
    # print(liit.brennt())
    # print(liit.get_anzahl_zutaten())
    # print(liit.beinhaltet_alkohol())
    # print(liit.menge_in_ml())

    root = SimplesGertaenk('rootb', rb)
    # print(root.brennt())
    # print(root.get_anzahl_zutaten())
    # print(root.beinhaltet_alkohol())
    # print(root.menge_in_ml())

    k = Registrierkasse()

    Registrierkasse.verkauft(k, root)
    Registrierkasse.verkauft(k, vget)
    Registrierkasse.verkauft(k, vc)
    Registrierkasse.verkauft(k, gin_otr)
    Registrierkasse.verkauft(k, apfel_pur)

    print(k._Registrierkasse__getraenkeliste)

    print(k.getraenke_sortiert())

    print(k.get_g_a_n_z())
