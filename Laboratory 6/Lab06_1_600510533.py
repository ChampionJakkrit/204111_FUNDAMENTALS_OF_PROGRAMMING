#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 1
# 204111 Sec 01A

def main():
    x = float(input())
    y = int(input())
    ans = int_power(x, y)
    # print("{0}".format(ans))
    print(ans)

def int_power(x, y):
    # ans = 1 # กำหนดค่าเริ่มต้น

    if y < 0:
        return 1 / (x**(-y)) # ถ้า y น้อยกว่า 0 ให้เท่ากับ 1 / (x**y)

    ans = 1 # กำหนดค่าเริ่มต้น
    for i in range (y):  # วนลูป y ครั้งด้วยการคูณ x เข้ากับผลลัพธ์เดิม
        ans *= x # ans = ans * x
    return ans # คืนค่าผลลัพธ์



if __name__ == '__main__':
    main()
