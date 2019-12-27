#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 05
# Problem 3
# 204111 Sec 01A


def main():
    d, m, y = map(int, input().split())  # รับค่า
    ans = count_down_to_songkran(d, m, y)
    print(ans)  # แสดงผล


def count_down_to_songkran(d, m, y):
    if m == 1:  # ถ้าเดือนไหนมห้ปวกต่อๆไปจนถึงวันสงกรานต์
        January = (31 - d) + leap_year(y) + 31 + 13
        return January

    elif m == 2:
        February = (leap_year(y) - d) + 31 + 13
        return February

    elif m == 3:
        March = (31 - d) + 13
        return March

    elif m == 4:
        if d <= 13:
            April = (13 - d)
            return April
        else:
            April = (30 - d) + 31 + 30 + 31 + 31 + 30 + 31 + \
                30 + 31 + 31 + leap_year(y + 1) + 31 + 13
            return April

    elif m == 5:
        May = (31 - d) + 30 + 31 + 31 + 30 + 31 + 30 + \
            31 + 31 + leap_year(y + 1) + 31 + 13
        return May

    elif m == 6:
        June = (30 - d) + 31 + 31 + 30 + 31 + 30 + \
            31 + 31 + leap_year(y + 1) + 31 + 13
        return June

    elif m == 7:
        July = (31 - d) + 31 + 30 + 31 + 30 + 31 + \
            31 + leap_year(y + 1) + 31 + 13
        return July

    elif m == 8:
        August = (31 - d) + 30 + 31 + 30 + 31 + 31 + leap_year(y + 1) + 31 + 13
        return August

    elif m == 9:
        September = (30 - d) + 31 + 30 + 31 + 31 + leap_year(y + 1) + 31 + 13
        return September

    elif m == 10:
        October = (31 - d) + 30 + 31 + 31 + leap_year(y + 1) + 31 + 13
        return October

    elif m == 11:
        November = (30 - d) + 31 + 31 + leap_year(y + 1) + 31 + 13
        return November

    elif m == 12:
        December = (31 - d) + 31 + leap_year(y + 1) + 31 + 13
        return December


def leap_year(year):  # ปีอธิกสุรทิน กุมภาพันะ์มี 29 วัน
    if (year % 400 == 0):  # หารเศษจาก 400 ลงตัว คืนค่า 29 วัน
        return 29

    else:  # หารเศษจาก 400 ไม่ลงตัวคืนค่า 28
        if (year % 4 == 0):  # หารเศษจาก 4 ลงตัว คืนค่า 28 วัน
            if (year % 100 != 0):  # หารเศษจาก 100 ไม่ลงตัว คืนค่า 29 วัน
                return 29
            else:
                return 28  # หารเศษจาก 100 ลงตัว คืนค่า 28 วัน
        else:  # หารเศษจาก 4 ไม่ลงตัว คืนค่า 28 วัน
            return 28
        return 28

if __name__ == '__main__':
    main()
