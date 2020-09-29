from pacTime import *
from OutMon import *
import unittest

class Test(unittest.TestCase):
    def test_pac(self):
        print("\ntest1: проверить ответ с datetime")
        self.assertEqual(diffDays('2018-06-07', '2020-12-08'),abs(datetime_days('2018-06-07', '2020-12-08')))

    def test_wrong(self):
        print("\ntest2: проверить не правилино форма")
        self.assertFalse(diffDays('000','2020-01-09'))

    def test_fab(self):
        print("\ntest3:проверить не правилино дата")
        self.assertFalse(diffDays('2020-02-31','2022-09-01'))

    def test_fab_29(self):
        print("\ntest4:проверить 02-29")
        self.assertEqual(abs(diffDays('2020-02-07', '2020-02-29')),abs(datetime_days('2020-02-07', '2020-02-29')))

    def test_wrong_SE(self):
        print("\ntest5:проверить start time > end time")
        self.assertEqual(diffDays('2020-12-08','2018-06-07' ),None)

    def test_workday(self):
        print("\ntest6:проверить на 2020-8 есть 21")
        self.assertEqual(work_days_count(2020,8) ,21)

    def test_mon(self):
        print("\ntest7:проверить на 2020-8 ")
        print(print_month(2020,8))
        # self.assertEqual()

    def test_mon_2(self):
        print("\ntest8:проверить на 2020-2 ")
        print(print_month(2020,2))

    def test_fab_Pac_end(self):
        print("\ntest9:проверить не правилино дата")
        self.assertFalse(diffDays('2020-02-01','2020-02-31'))

    def test_wrong_end(self):
        print("\ntest10:проверить не правилино форма")
        self.assertFalse(diffDays('2020-01-01','2022'))




if __name__ =='__main__':
    unittest.main()