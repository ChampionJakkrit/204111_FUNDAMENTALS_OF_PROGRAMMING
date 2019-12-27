# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 5
# 204111 Sec 01A
import math

def main():
    number = int(input()) # รับค่าจากผู้ใช้
    k = int(input())
    value = int(input())
    ans = set_kth_digit(number, k, value)
    print("%d"%ans) # แสดงค่า
    
def kth_digit(number, k):
    c = (abs(number) // 10**k) % 10 # อ้างอิงจาก ข้อ 4
    return c

def set_kth_digit(number, k, value):
    a = kth_digit(number, k) * 10**k
    b = (number - a) + value * 10**k # นำจำนวนมาลบให้ = 0 เพื่อจะ + ค่าใหม่ที่ต้องการใส่เข้าไป

    return b
    
if __name__ == '__main__' :
    main()
