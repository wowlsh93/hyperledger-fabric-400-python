# coding=utf-8
import time
import datetime


def getCurrentClock():
    return time.time()


def getCurrentStrDate():
    return time.strftime("%Y-%m-%d")


def getCurrentStrTime():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def getCurrentStrSecTime():
    t = getCurrentClock()
    tmicsec = t - int(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)) + ".{:03d}".format(int(tmicsec * 1000))


def getTickStrSecTime(t):
    tmicsec = t - int(t)
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)) + ".{:03d}".format(int(tmicsec * 1000))


def getClockElement(tTime):
    return [
        getDateTimeFromIndex(tTime, 0),
        getDateTimeFromIndex(tTime, 1),
        getDateTimeFromIndex(tTime, 2),
        getDateTimeFromIndex(tTime, 3),
        getDateTimeFromIndex(tTime, 4),
        getDateTimeFromIndex(tTime, 5)
    ]


def getCurrentPowerAllStrTime():
    return time.strftime("%Y-%m-%d %H")


def getStrTime(tTime):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tTime))


def getDiffTime2(tTime1, tTime2):
    return tTime2 - tTime1


def getDiffTime(tTime):
    return getCurrentClock() - tTime


"""
    '2014-08-13 11:06:44' 인 경우
    getDateTimeFromIndex
    0 : 2014
    1 : 8
    2 : 13
    3 : 11
    4 : 6
    5 : 44
    그외 요일 등
"""


def getDateTimeFromIndex(tTime, nIdx):
    return time.localtime(tTime)[nIdx]


def getTimeFromDateTime(dtTime):
    return time.mktime(dtTime.timetuple())  # + dtTime.microsecond / 1E6


def getTimeFromEachValue(nYear, nMonth, nDay):
    return getTimeFromDateTime(datetime.date(nYear, nMonth, nDay))


def getDateTimeFromTime(tTime):
    return datetime.datetime.fromtimestamp(time.mktime(time.localtime(tTime)))


def getDateTimeFromString(szTime):
    return datetime.datetime.strptime(szTime, "%Y-%m-%d %H:%M:%S")


def getDateTimeUTCFromString(szTime):
    return datetime.datetime.strptime(szTime, "%Y-%m-%dT%H:%M:%S") + datetime.timedelta(hours=9)


def addDayToDateTime(dtTime, nDay):
    return dtTime + datetime.timedelta(days=nDay)


def addHourToDateTime(dtTime, nHour):
    return dtTime + datetime.timedelta(hours=nHour)


# datetime 타입을 입력해서 누적초를 리턴
def convertDatetimeToSec(dtTime):
    return dtTime.total_seconds()


# 초를 입력해서 3분:30초 같은 문자열로 리턴
def convertSecToStr(s):
    m = int(s / 60)
    ss = int(s % 60)
    return "{}분:{}초".format(m, ss)
