#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 05
# Problem 5
# 204111 Sec 01A


def main():
    year = int(input()) # รับค่า
    ans = zodiac_element(year)
    print(ans) # แสดงผล


def zodiac_element(year): # ราศี

    if year % 12 == 0:   # หารเศษจากปี เหลือ 0 คืนค่า Money
        return (Element(year) + (" Monkey")) 

    elif year % 12 == 1:        
        return (Element(year) + (" Rooster"))  # หารเศษจากปี เหลือ 1 คืนค่า Money

    elif year % 12 == 2:
        return (Element(year) + (" Dog"))  # หารเศษจากปี เหลือ 2 คืนค่า Dog

    elif year % 12 == 3:
        return (Element(year) + (" Pig"))  # หารเศษจากปี เหลือ 3 คืนค่า Pig 

    elif year % 12 == 4:
        return (Element(year) + (" Rat"))  # หารเศษจากปี เหลือ 4 คืนค่า Rat

    elif year % 12 == 5:
        return (Element(year) + (" Ox"))  # หารเศษจากปี เหลือ 5 คืนค่า Ox

    elif year % 12 == 6:
        return (Element(year) + (" Tiger"))  # หารเศษจากปี เหลือ 6 คืนค่า Tiger

    elif year % 12 == 7:
        return (Element(year) + (" Rabbit"))  # หารเศษจากปี เหลือ 7 คืนค่า Rabbit

    elif year % 12 == 8:
        return (Element(year) + (" Dragon"))  # หารเศษจากปี เหลือ 8 คืนค่า Dragon

    elif year % 12 == 9:
        return (Element(year) + (" Snake"))  # หารเศษจากปี เหลือ 9 คืนค่า Snake

    elif year % 12 == 10:
        return (Element(year) + (" Horse"))  # หารเศษจากปี เหลือ 10 คืนค่า Horse

    elif year % 12 == 11:
        return (Element(year) + (" Goat"))  # หารเศษจากปี เหลือ 11 คืนค่า Goat


def Element(year): # ธาตุ
    if year % 10 == 0 or year % 10 == 1: # หารเศษจาก 10 เหลือ 0 หรือ 1 คืนค่า Matel (ธาตุชนิดที่ 1)
        return ("Metal")

    elif year % 10 == 2 or year % 10 == 3:  # หารเศษจาก 10 เหลือ 2 หรือ 3 คืนค่า Water (ธาตุชนิดที่ 2)
        return ("Water")

    elif year % 10 == 4 or year % 10 == 5:  # หารเศษจาก 10 เหลือ 4 หรือ 5 คืนค่า Wood (ธาตุชนิดที่ 3)
        return ("Wood")

    elif year % 10 == 6 or year % 10 == 7:  # หารเศษจาก 10 เหลือ 6 หรือ 7 คืนค่า Fire (ธาตุชนิดที่ 4)
        return ("Fire")

    elif year % 10 == 8 or year % 10 == 9:  # หารเศษจาก 10 เหลือ 8 หรือ 9 คืนค่า Earth (ธาตุชนิดที่ 5)
        return ("Earth") 


if __name__ == '__main__':
    main()
