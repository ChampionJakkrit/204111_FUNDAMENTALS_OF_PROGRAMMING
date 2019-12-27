# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 4
# 204111 Sec 01A
import math

def main():
    number = int(input()) # รับค่าจากผู้ใช้
    k = int(input())
    ans = kth_digit(number, k)
    print("%d"%ans) # แสดงค่า

def kth_digit(number, k):
    c = (abs(number) // 10**k) % 10 # แปลงค่า

    return c

if __name__ == '__main__' :
    main()
    
    
    
