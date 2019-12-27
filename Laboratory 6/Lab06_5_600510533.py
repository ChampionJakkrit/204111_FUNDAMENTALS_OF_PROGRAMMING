#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 2
# 204111 Sec 01A

def main():
    n = int(input())
    ans  = longest_digit_run(n)
    print(ans)

def longest_digit_run(n):
    last = -1 # กำหนดค่าล่าสุด (ค่าที่ไม่ใช่ 0-9)
    line = 1 # กำหนดความยาว
    most = 1 # กำหนดค่าสูงสุด
    while n != 0:
        present = n % 10 # จะได้ค่าปัจจุบันเป็นเลขหลักเดียว (0-9)
        if present == last : # ถ้าค่าปัจจุบันเท่ากับค่าน้อยๆ
            line = line + 1 
        else: # ถ้าไม่ใช่ line จะ = 1
            line = 1
            last = present # อัพเดตค่า
        most = max(most, line)
        n //= 10 # จะได้เลขหลักเดียวที่น้อยลงเรื่อยๆเรียงตามหลัก

    return most

if __name__ == '__main__' :
    main()