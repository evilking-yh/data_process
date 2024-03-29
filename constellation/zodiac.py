#coding:utf-8

def chinese_zodiac1(year):
    return u'猴鸡狗猪鼠牛虎兔龙蛇马羊'[year % 12]


def zodiac(month, day):
    n = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
    d = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22), (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))
    return n[len(list(filter(lambda y: y <= (month, day), d))) % 12]

def chinese_zodiac(year):
    zodiac_map = {
        u'鼠': 1900,
        u'牛': 1901,
        u'虎': 1902,
        u'兔': 1903,
        u'龙': 1904,
        u'蛇': 1905,
        u'马': 1906,
        u'羊': 1907,
        u'猴': 1908,
        u'鸡': 1909,
        u'狗': 1910,
        u'猪': 1911
    }

    for k, v in zodiac_map.items():
        if (year % v % 12) == 0:
            return k

print(chinese_zodiac1(1900))
print(zodiac(7, 5))



