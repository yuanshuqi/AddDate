def dateAbs(a, b):
    # 计算日期差 вычислить разница дата
    return (a - b) - 1


def isLeap(year):
    # 判断是否闰年 проверить високосный год или нет
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        return 1
    else:
        return 0


def Days(y, m, d):
    # 判断某个日期从年初（y年1月1日）到该天（y年m月d天）的天数 проверить число дней с начала год до это число дата
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0
    if isLeap(y):
        days[2] = 29
    for i in days[0:m]:
        sum = sum + i
    sum = sum + d

    return sum

import re
def diffDays(start_day, end_day):
    # 计算两个日期之间的天数 вычислить разница
    value = re.compile("[0-9][0-9][0-9][0-9]-[0-1][0-9]-[0-3][0-9]")
    result = value.match(start_day)
    if not result:
        print("起始日期格式输入错误")
        return
    result = value.match(end_day)
    if not result:
        print("结束日期格式输入错误")
        return
    y1 = int(start_day.split("-")[0])
    m1 = int(start_day.split("-")[1])
    d1 = int(start_day.split("-")[2])

    y2 = int(end_day.split("-")[0])
    m2 = int(end_day.split("-")[1])
    d2 = int(end_day.split("-")[2])

    sum = 0
    if y1 == y2:
        # 如果：同年不同月不同日 если это год одиного ну разный мясяца и разный день
        s1 = Days(y1, m1, d1)
        s2 = Days(y2, m2, d2)
        sum = dateAbs(s1, s2) + 1
        return sum

    elif y1 < y2:
        count = y2 - y1

        t1 = Days(y1, m1, d1)
        t2 = Days(y2, m2, d2)

        p1 = Days(y1, 12, 31) - t1

        sum = 0
        for i in range(count - 1):
            sum = sum + Days(y1 + i, 12, 31)
        p2 = sum
        p3 = t2 - 1
        sum = p1 + p2 + p3 + 1
        return -sum
    else:
        temp = y1, m1, d1
        y1, m1, d1 = y2, m2, d2
        y2, m2, d2 = temp
        start_day = str(y1) + "-" + str(m1) + "-" + str(d1)
        end_day = str(y2) + "-" + str(m2) + "-" + str(d2)
        return -diffDays(start_day, end_day)

#
#
start_day = input("вводите раннюю дату(формат:xxxx-xx-xx):")
end_day = input("вводите поздняя дату(формат:xxxx-xx-xx):")



print("разница дата(я писала):", diffDays(start_day, end_day))

#проверить ответ
import datetime


def datetime_days(str1, str2):
    date1 = datetime.datetime.strptime(str1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(str2, "%Y-%m-%d")
    num = (date1 - date2).days
    return num


print("разница дата(with datetime):", datetime_days(start_day, end_day))

if datetime_days(start_day,end_day)== diffDays(start_day, end_day):
    print("ответ правило!")