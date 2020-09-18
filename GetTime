import datetime

def GetNow():
    TimeNow = datetime.datetime.now().strftime('20%y-%b-%d %H:%M:%S')
    print('сейчас:', TimeNow)
    return TimeNow

def GetTime():
    tday = datetime.date.today()
    print('сегодня:', tday)
    return tday

def AfterWeeks(time):
    AddWeeks = datetime.timedelta(days=7)
    TimeAWeeks = time + AddWeeks
    print('Дата (после неделю):', TimeAWeeks)
    return TimeAWeeks

GetNow()
GetTime()
AfterWeeks(GetTime())