import unittest
from uebungen.ueblatt_8 import Office, Flat, House, Accounting


class OfficeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.office = Office(150, 30)

    def test_calc_lease(self):
        erg = self.office.calc_lease()
        self.assertEqual(erg, 1200, "Lease incorrectly calculated")


class FlatTest(unittest.TestCase):

    def setUp(self) -> None:
        self.flat1 = Flat(124, 4, "High")
        self.flat2 = Flat(81, 3, "Standard")
        self.flat3 = Flat(55, 2, "Low")

    def test_calc_lease_flat1(self):
        erg = self.flat1.calc_lease()
        self.assertEqual(erg, 1040, "Lease incorrectly calculated")

    def test_calc_lease_flat2(self):
        erg = self.flat2.calc_lease()
        self.assertEqual(erg, 637.5, "Lease incorrectly calculated")

    def test_calc_lease_flat3(self):
        erg = self.flat3.calc_lease()
        self.assertEqual(erg, 385, "Lease incorrectly calculated")


class HouseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.house = House(158, True)

    def test_calc_lease(self):
        erg = self.house.calc_lease()
        self.assertEqual(erg, 1780, "Lease incorrectly calculated")


# Ich habe hier auch für Accounting einen Test geschrieben, aber es wird nicht erkannt und durchgelaufen.
# Keine Ahnung warum.
#
# class AccountingTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.account = Accounting()
#
#     def overall_lease_test(self):
#         office = Office(150, 30)
#         flat1 = Flat(124, 4, "High")
#         flat2 = Flat(81, 3, "Standard")
#         flat3 = Flat(55, 2, "Low")
#         self.account.add(office)
#         self.account.add(flat1)
#         self.account.add(flat2)
#         self.account.add(flat3)
#         erg = self.account.get_overall_lease()
#         self.assertEqual(erg, 3262.5, "Lease incorrectly calculated")

if __name__ == '__main__':
    unittest.main()
