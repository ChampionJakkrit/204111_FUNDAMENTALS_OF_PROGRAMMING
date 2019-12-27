#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 5
# 204111 Sec 01A

import math

def main():
    num = int(input())
    pos = int(input())
    ans = rotate(num, pos)
    print(ans)

def rotate(num, pos):
    #สมมุติ 
    #num = 12345
    #pos = 3
    x = pos # กำหนดให้ไปพิจารณาลบ
    lenght = int(math.log10(num)) + 1 # หาความยาวของจำนวน num
    pos = abs(pos) % lenght # ตำแหน่ง
    if x >= 0:
        after = num % 10 ** pos # หาจำนวน 3 ตัวหลัง ater = 345
        before = num // 10 ** pos # หารเพื่อให้เหลือจำนวนหน้า before = 12
        after = after * 10**(lenght-pos) # แปลงตัวเลขข้างหลังให้ไปอยู่ข้างหน้า ater = 34500
        return after + before # ผลรวม = 34512

    else: # กรณีลบ
        after = num % 10 ** (lenght - pos)  # หาตัวเลข 2 ตัวหลัง afer = 45
        before = num // 10 ** (lenght - pos) # หารแล้วจะเหลือเลขข้างหน้า before = 123
        after = after * 10**(pos) # แปลงตัวเลขข้างหลังให้ไปอยู่ข้างหน้า ater = 45000
        return after + before # ผลรวม = 45123



if __name__ == '__main__':
    main()