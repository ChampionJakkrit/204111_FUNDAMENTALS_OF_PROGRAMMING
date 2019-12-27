#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 1
# 204111 Sec 01A

import math

def main():
    x = int(input())
    y = int(input())
    ans = sum_prime_in_range(x, y)
    print(ans)

def sum_prime_in_range(x, y):
    sum_ = 0
    for i in range(x,y+1,1): # วนตั้งแต่ 1 ถึง y
        if(factorize(i)): # ส่งไปหาฟังก์ชันว่า i ใช่เป็นจำนวนเฉพาะรึป่าว
            sum_ = sum_ + i # ถ้าเป็นจำนวนเฉพาะให้บวกรวม
    return sum_


def factorize(x):
   
    for i in range(2, int(x**0.5) + 1, 1): # เช็คว่าเป็นจำนวนเฉพาะหรือไม่ ถ้าตัวอื่นหารตัวมันลงตัวจะไม่เป็นจำนวณเฉพาะ
        if x % i == 0:
            bound = int(x**0.5) + 1

            while i < bound : # วนตัวประกอบที่เป็นไปได้
                while x % i == 0 : # แสดงตัวประกอบของจำนวนของ x
                    x //= i # ถ้าจำนวนในตัวประกอบหารตัวมันเอง ไม่เท่ากับ 1 จะใส่ * (แต่ เช่น 15 = 15/15 = 1 จะเป็นตัวสุดท้าย)
                    
                    if x != 1:
                        pass
                    else :
                        return 0
                i += 1
            if x != 1:
                return 0


    return 1      
                   

if __name__ == '__main__':
    main()