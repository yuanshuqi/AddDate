import unittest
from pacTime import *
from OutMon import *
class TestPacTime(unittest.TestCase):
    def test_pac(self):
        start_day = "2018-06-07"
        end_day = '2020-12-08'
        print('\r')
        print('№1  test разница с дата :')
        my = diffDays(start_day, end_day)
        print("разница дата(я писала):", my)
        usepip = abs(datetime_days(start_day, end_day))
        print("разница дата(with datetime):", usepip)

        if my == usepip:
            print("ответ правило!")
        else:
            print("ответ не правило!")

    def test_mon(self):
        YearNum = 2020
        MonNum = 8
        print('\r')
        print('№2  календарь и робочий день :')
        print_month(YearNum,MonNum)
        print('\r')
        count = work_days_count(YearNum, MonNum)
        print(f'день для работа в {YearNum}-{MonNum} есть {count}дня!')

    def test_wrongFop(self):
        start_day = "000"
        end_day = '20201208'
        print('\r')
        print('№3  test не правило дата :')
        diffDays(start_day, end_day)
        # datetime_days(start_day, end_day)

    def test_fab(self):
        start_day = "2020-02-31"
        end_day = '2020-12-08'
        print('\r')
        print('№4  test не правилиный дата :')
        diffDays(start_day, end_day)
        # datetime_days(start_day, end_day)





if __name__ =='__main__':
    unittest.main()
