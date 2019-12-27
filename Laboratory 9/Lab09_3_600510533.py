#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 3
# 204111 Sec 01A

def main():
    patterned_message("123", "** *** ** ** *")

    patterned_message("D and C",'''
***************
******   ******
***************
''')

    patterned_message("Three Diamonds!",'''
  *     *     *
 ***   ***   ***
***** ***** *****
 ***   ***   ***
  *     *     *
''')


def patterned_message(message, pattern):
    new_m = "" # สร้างตัวอักษรใหม่
    for ch in message :
        if ch != ' ':
            new_m += ch
    message = new_m + ""
    index = 0
    for item in pattern.splitlines(): # แยกบรรทัด
        for character in item: # วนหาตัวที่เป็น"*" ถ้าเป็นให้แสดงผล index ของ message
            if character == '*' : 
                print(message[index], end = '')
                index += 1
                if (index >= len(message)): # ถ้าความยาวเกินตัวอักษรของ message ให้วนที่ 0 ใหม่
                    index = 0
            else: # ถ้าไม่ใช่ให้แสดง ช่องว่างแทน
                print(" ", end = '')
        print()

        




if __name__ == '__main__':
    main()