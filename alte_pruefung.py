import abc
import math
from typing import List, Dict


class Instrument:
    def __init__(self, name: str, lautstaerke: float):
        self.name = name
        self.lautstaerke = lautstaerke


class Musikant(abc.ABC):
    def __init__(self, anzahl_beine: int, instrument: Instrument):
        self.__anzahl_beine = anzahl_beine
        self.__instrument = instrument

    @property
    def anzahl_beine(self):
        return self.__anzahl_beine

    @property
    def instrument(self):
        return self.__instrument

    @abc.abstractmethod
    def verscheuche_raeuber(self) -> int:
        pass

    @abc.abstractmethod
    def spiele_musik(self) -> float:
        pass

    def __repr__(self):
        return f' Verscheucht: {self.verscheuche_raeuber()}, Musiziert: {self.spiele_musik()}'


class Esel(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, tritt_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__tritt_kraft = tritt_kraft

    @property
    def tritt_kraft(self):
        return self.__tritt_kraft

    def __repr__(self):
        return f'{type(self).__name__} {self.__tritt_kraft} {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        x = math.floor(self.__tritt_kraft * self.anzahl_beine)
        return x

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke


class Hund(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, bell_lautstaerke: float):
        super().__init__(anzahl_beine, instrument)
        self.__bell_lautstaerke = bell_lautstaerke

    @property
    def bell_lautstaerke(self):
        return self.__bell_lautstaerke

    def __repr__(self):
        return f'{type(self).__name__} {self.__bell_lautstaerke} {format(super().__repr__())}'

    # beim Hund war es nicht angegeben, wie man die Anzahl von Räuber ausrechet
    def verscheuche_raeuber(self) -> int:
        return 1

    def spiele_musik(self) -> float:
        return (self.__bell_lautstaerke + self.instrument.lautstaerke) / 2


class Katze(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, kratz_kraft: float):
        super().__init__(anzahl_beine, instrument)
        self.__kratz_kraft = kratz_kraft

    @property
    def kratz_kraft(self):
        return self.__kratz_kraft

    def __repr__(self):
        return f'{type(self).__name__} {self.__kratz_kraft} {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.anzahl_beine == 4:
            x = math.floor(self.__kratz_kraft)
        elif self.anzahl_beine == 3:
            x = math.floor(self.__kratz_kraft / 2)
        else:
            x = 1
        return x

    def spiele_musik(self) -> float:
        return self.instrument.lautstaerke


class Hahn(Musikant):
    def __init__(self, anzahl_beine: int, instrument: Instrument, flug_weite: float):
        super().__init__(anzahl_beine, instrument)
        self.__flug_weite = flug_weite

    @property
    def flug_weite(self):
        return self.__flug_weite

    def __repr__(self):
        return f'{type(self).__name__} {self.__flug_weite} {format(super().__repr__())}'

    def verscheuche_raeuber(self) -> int:
        if self.__flug_weite < 2:
            x = self.instrument.lautstaerke
        elif math.floor(self.__flug_weite) == 2:
            x = 6
        elif math.floor(self.__flug_weite) == 3:
            x = 5
        elif math.floor(self.__flug_weite) == 4:
            x = 4
        elif math.floor(self.__flug_weite) == 5:
            x = 3
        elif math.floor(self.__flug_weite) == 6:
            x = 2
        else:
            x = 1
        return math.floor(x)

    def spiele_musik(self) -> float:
        return (self.instrument.lautstaerke + 2) / self.__flug_weite


class Quartett:
    def __init__(self):
        self.__musikantenliste = []

    def add_musikant(self, m: Musikant):
        self.__musikantenliste.append(m)

    def ist_quartett(self) -> bool:
        return len(self.__musikantenliste) == 4

    def gemeinsam_raeuber_verscheut(self) -> int:
        y = 0
        for x in range(len(self.__musikantenliste)):
            y += self.__musikantenliste[x].verscheuche_raeuber()
        return y

    def durchschnittliche_lautstaerke(self) -> float:
        y = 0
        for x in range(len(self.__musikantenliste)):
            y += self.__musikantenliste[x].spiele_musik()
        z = y / len(self.__musikantenliste)
        return z

    def get_m_in_ls_bereich(self, von: float, bis: float) -> List[Musikant]:
        ls_liste = []
        for x in range(len(self.__musikantenliste)):
            if von <= self.__musikantenliste[x].spiele_musik() <= bis:
                ls_liste.append(self.__musikantenliste[x])
                # so liefert das eine Liste mit die __repr__s von den Objekte. Braucht man hier die Variablen? Wie
                # zB. "esel"?
        return ls_liste

    def get_anz_m_mit_bein_anz(self) -> Dict[int, int]:
        bein_dict = {}
        for x in range(len(self.__musikantenliste)):
            if self.__musikantenliste[x].anzahl_beine in bein_dict:
                bein_dict[self.__musikantenliste[x].anzahl_beine] += 1
            else:
                bein_dict[self.__musikantenliste[x].anzahl_beine] = 1
        return bein_dict


if __name__ == '__main__':
    flt = Instrument('Floete', 6.1)
    geige = Instrument('Geige', 2.5)
    gtr = Instrument('Gitarre', 4.8)
    bass = Instrument('Bassgitarre', 3.8)

    esel = Esel(4, flt, 2.6)
    hund = Hund(4, geige, 8.1)
    katze = Katze(3, gtr, 4.1)
    hahn = Hahn(2, bass, 1.9)

    # print(esel.verscheuche_raeuber())
    # print(hund.verscheuche_raeuber())
    # print(katze.verscheuche_raeuber())
    # print(hahn.verscheuche_raeuber())

    # print(esel.spiele_musik())
    # print(hund.spiele_musik())
    # print(katze.spiele_musik())
    # print(hahn.spiele_musik())

    # print(esel)

    q = Quartett()
    q.add_musikant(esel)
    q.add_musikant(hahn)
    q.add_musikant(katze)
    q.add_musikant(hund)

    print(q.ist_quartett())
    print(q.gemeinsam_raeuber_verscheut())
    print(q.durchschnittliche_lautstaerke())
    print(q.get_m_in_ls_bereich(4.9, 6.8))
    print(q.get_anz_m_mit_bein_anz())
