import unittest

from uebungen.ueblatt6_bsp2 import Registrierkasse, SimplesGertaenk, LongDrink, Cocktail, Fluessigkeit


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.k = Registrierkasse()
        apfelsaft = Fluessigkeit('apfelsaft', 200, 0)
        cola = Fluessigkeit('cola', 150, 0)
        vodka = Fluessigkeit('vodka', 5, 40)
        gin = Fluessigkeit('gin', 5, 40)
        eistee = Fluessigkeit('eistee', 100, 0)
        rb = Fluessigkeit('rootbeer', 330, 0)
        apfel_pur = SimplesGertaenk('apfel_pur', apfelsaft)
        gin_otr = SimplesGertaenk('gin_otr', gin)
        vc = LongDrink('vodka_mit_cola', vodka, cola)
        vget = Cocktail('vodka_gin_eistee', [vodka, gin, eistee])
        root = SimplesGertaenk('rootb', rb)
        self.k.verkauft(root)
        self.k.verkauft(vget)
        self.k.verkauft(vc)
        self.k.verkauft(gin_otr)
        self.k.verkauft(apfel_pur)

    def test_verkauft_anzahl_stimmt(self):
        self.assertEqual(self.k._Registrierkasse__verkaufte_getraenke, 5, "Ooops")

    # # Diese hier fnktioniert nicht, wäre sehr dankbar wenn jemand mir erklären könnte warum nicht
    # def test_verkauft_liste_stimmt(self):
    #     liste = [rootb, vodka_gin_eistee, vodka_mit_cola, gin_otr, apfel_pur]
    #     self.assertListEqual(self.k._Registrierkasse__getraenkeliste,liste,"Ooops")


if __name__ == '__main__':
    unittest.main()
