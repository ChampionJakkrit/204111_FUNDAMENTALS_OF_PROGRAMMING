#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 4
# 204111 Sec 01A


def main():
    total = int(input("Total students: "))
    n = 0
    max_ = 0  # กำหนดค่าเริ่มต้น
    mid_ = 0
    print("Enter score:")
    
    for e in range(total):
        i = int(input())

        n = n + i  # ผลรวมทั้งหมดที่รับมา

        if i > max_:  # หาค่าสูงสุด
            mid_ = max_ # แทนค่า i วนลูปไปเรื่อยๆจนครบเทียบจากค่าสูงสุด = 0 แล้วจะได้ค่าสูงสุด
            max_ = i
            # ถ้าไม่เข้ากรณี if จะมาเข้า elif ต่อ

        elif i > mid_ and i != max_: # (หาค่ารอง) ถ้า จำนวนที่ใส่มา > ค่ารอง และ จำนวน ไม่เท่ากับ ค่าสูงสุด
            mid_ = i # ค่ากลางจะเท่ากับค่ากลางของจำนวนที่ใส่มา

    avr = n / total  # หาค่าเฉลี่ย
    print("---")
    print("Max score is: %.2f " % max_) # แสดงผล

    if mid_ == 0: # ถ้าค่ารอง = 0 แสดงผลเป็น None
        print("Runner up is: None")
    else:
        print("Runner up is: %.2f " % mid_)
    print("Average is: %.2f " % avr)

main()
