#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 5
# 204111 Sec 01A

import string
def main():
    decode("aceiklmr-",'''
3
5 3 4 2
3 1 2 8 1 7 2 0 86
''')

def decode(code_table, text):
    for line in text.splitlines(): # แยกบรรทัด
        line.split(" ")
        for item in line.split():
            int_ = int(item) # แปลง string เป็น int

            if 0 <= int_ < len(code_table) : # ถ้าค่ามากว่าหรือเท่ากับ 0 แต่น้อยกว่าความยาวของข้อความ
                print(code_table[int_], end = "") # แสดงผล index ของตำแหน่งนั้นๆ

            else:
                print("_", end = "") # ถ้ามากกว่าหรือน้อยกว่านั้นอสดงผล "_"

        print("")



if __name__ == '__main__':
    main()
