#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 3
# 204111 Sec 01A

def main():
    x = int(input())
    factorize(x)

def factorize(x):
    if x < 2 :
        print(x, "is", x)
        return

    for i in range(2, int(x**0.5) + 1, 1): # เช็คว่าเป็นจำนวนเฉพาะหรือไม่ ถ้าตัวอื่นหารตัวมันลงตัวจะไม่เป็นจำนวณเฉพาะ
        if x % i == 0: # ตัวที่หาร x ลงตัว i เป็นตัวประกอบของ x
            print("%d is "%x, end="")

            bound = int(x**0.5) + 1
            while i < bound : # วนตัวประกอบที่เป็นไปได้
                while x % i == 0 : # แสดงตัวประกอบของจำนวนของ x
                    print(i,"", end="")
                    x //= i 
                    
                    if x != 1:  # ถ้าจำนวนในตัวประกอบหารตัวมันเอง ไม่เท่ากับ 1 จะใส่ * (แต่ เช่น 15 = 15/15 = 1 จะเป็นตัวสุดท้าย)
                        print("* ", end="")
                    else :
                        print("")
                        return 
                i += 1
            if x != 1:
                print(x)
            return 


    print("%d is prime"%x)
    return     





if __name__ == '__main__':
    main()