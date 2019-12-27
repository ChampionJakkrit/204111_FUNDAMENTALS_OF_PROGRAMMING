#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 10
# Problem 1
# 204111 Sec 01A

import string
def main():
    str1 = input() # รับค่า
    str2 = input()
    ans = is_anagram(str1, str2)
    print(ans)

def is_anagram(str1, str2):
    list_str1 = []
    list_str2 = []
    str1 = str1.lower() # ทำให้เป็นตัวเล็กทั้งหมด
    str2 = str2.lower()
    for item in str1:
        if item in string.ascii_letters: # ทำก็ต่อเมื่อเป็น str
            list_str1.append(item) # ทำเป็น list
    for utem in str2:
        if utem in string.ascii_letters: # ทำก็ต่อเมื่อเป็น str
            list_str2.append(utem) # ทำเป็น list

    list_str1.sort() # เรียงจาก a - z
    list_str2.sort() # เรียงจาก a - z

    if list_str2 == list_str1: # ถ้า list str 2 = list str1
        return True 
    else:
        return False


if __name__ == '__main__':
    main()