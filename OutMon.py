
#按上R执行它或将其替换为您的代码。
#按Double上在各处搜索类，文件，工具窗口，操作和设置。

months_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week_days_name = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

#确定这一年之前到公元元年的天数
def days_before_year(year):
    # 确定整年的数量
    y = year - 1
    return y * 365 + y // 4 - y // 100 + y // 400


#确定该年这一月份到年初的天数
def days_before_month(year, month):
    days = 0
    for day in range(month - 1):
        days += days_in_month[day]
    if month > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        days += 1
    return days



# 外推格里历（proleptic Gregorian calendar） 01-Jan-0001 as day 1
#return 到 01-Jan-0001的天数
def days_in_pgc(year, month, day):

    #如果要是闰年的二月份的话 days=29；若不是则正常算
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        days = 29
    else:
        days = days_in_month[month - 1]
    # if day < 1 or day > days:
    #     print(f'day must be bigger than 0 and smaller than {days + 1}')

    return days_before_year(year) + days_before_month(year, month) + day


#这一天是周几
def week_day(year, month, day):
    "Return day of the week, where Monday == 0 ... Sunday == 6."
    return (days_in_pgc(year, month, day) + 6) % 7



def print_month(year, month):
    print('       'f'{months_name[month - 1]} {year}')
    print("---------------------------")


    #打印日历的星期的标 周一周二。。
    week_day_name_list = ''
    for week_day_name in week_days_name:
        week_day_name_list += week_day_name[:3] + ' '
    print(week_day_name_list)

    #按照该月的天数进行打印  几月就打多少天的
    if month == 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        days = 29
    else:
        days = days_in_month[month - 1]

    for day in range(days):
        day_in_week = week_day(year, month, day + 1)
        if day == 0:
            for dayi in range(day_in_week):
                print(f'    ', end="")

        print("%3d " % (day + 1), end="")
        if day_in_week + 1 == 7:
            print('\r')


def work_days_count(year, month):
    count = 0
    days = days_in_month[month - 1]
    for day in range(days):
        day_in_week = week_day(year, month, day + 1)
        if 0 <= day_in_week <= 4:
            count += 1
    return count

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # is_valid('PyCharm')
    # for month in range(12):
    #     print(f'days_before_month: {days_before_month(2020, month + 1)}')

    # print(f'days_before_month: {days_before_month(2020, 1)}')
    # weekday(2020, 9, 12)
    # ###############################
    # print_month(2020, 8)
    # print('\r')
    # count = work_days_count(2020, 8)
    # print(f'work days in 2020-9 is {count}')

    ####################################################################################
    # YearNum = int(input("вводите номер год:"))
    # MonNum = int(input("вводите номер месяца:"))
    # print_month(YearNum,MonNum)
    # print('\r')
    # count = work_days_count(YearNum, MonNum)
    # print(f'work days in {YearNum}-{MonNum} is {count}')


    # print("以下输出2016年1月份的日历:")
    # calendar.prmonth(2016, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
