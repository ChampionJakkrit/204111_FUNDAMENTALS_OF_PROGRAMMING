#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 4
# 204111 Sec 01A

def main():
    n = int(input())
    ans = life_path(n)
    print(ans)

def life_path(n):
    int_ = 0
    while n > 9:
        while n != 0:
            present = n % 10 #จะได้ค่าที่เป็นหลักหน่วยมา
            int_ += present
            n //= 10 # เปลี่ยนจากหลักอื่นเป็นหลักหน่วย
        n = int_
        int_ = 0
    return n
   
if __name__ == '__main__':
    main()