#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 4
# 204111 Sec 01A

import string
def main():
    line = input()
    print(uniform(line))

def uniform(line):
    count_lower = 0
    count_upper = 0

    for item in line:
        if item in string.ascii_letters: # ถ้าเป็นตัวอักษรเท่านั้น
            if item in string.ascii_lowercase: # ถ้าเป็นอักษรตัวเล็ก ให้นับเก็บไว้ทีละ 1
                count_lower += 1
            elif item in string.ascii_uppercase: # ถ้าเป็นอักษรตัวใหญ่ ให้นับเก็บไว้ทีละ 1
                count_upper += 1

    if count_upper > count_lower: # ถ้าตัวใหญ่มากกว่าตัวเล็ก ให้คืนค่าตัวใหญ่ทั้งหมด
        return line.upper()
    elif count_upper == count_lower: # ถ้าตัวใหญ่เท่ากับตัวเล็ก
        if line[0] in string.ascii_lowercase: # ถ้าตัวหน้าสุดเป็นตัวเล็ก ให้คืนค่าตัวเล็กทั้งหมด
            return line.lower()
        else: # ถ้าตัวหน้าสุดเป็นตัวใหญ่ ให้คืนค่าตัวใหญ่ทั้งหมด
            return line.upper()
    else: # ถ้าตัวใหญ่น้อยกว่าตัวเล็ก ให้คืนค่าตัวเล็กทั้งหมด
        return line.lower()
        

if __name__ == '__main__':
    main()