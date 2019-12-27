#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 3
# 204111 Sec 01A

def main():
    n = int(input())
    triangle(n)


def triangle(n):

    for i in range(n):
        for j in range(i*2+1):
            if i == n-1: # ฐาน
                if j % 2 == 0:  # ถ้าเป็น 0 2 4 6 8 (เลขคู่) ปริ้น "*"
                    print("*",end = "")
                else: # ถ้าเป็น 1 3 5 7 9 (เลขคี่) ปริ้นช่องว่าง
                    print(" ",end = "")
                continue # ข้ามการทำฐานไปก่อน
            if j == 0 or j == i*2: # หลักแรก กับหลักเฉียง ปริ้น "*"
                print("*",end = "")
            else: # ข้างใน ปริ้น "."
                print(".",end = "")
        print("")

if __name__ == '__main__':
    main()

