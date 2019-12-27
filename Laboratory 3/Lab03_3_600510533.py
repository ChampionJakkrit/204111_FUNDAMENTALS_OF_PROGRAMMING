#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 3
# 204111 Sec 01A

def main():
    x = float(input()) # รับค่าจากผู้ใช้
    c = octagon_area(x)
    print("%.6f"%c) # แสดงค่า

def octagon_area(x):
    square = x * x # สูตรสี่เหลี่ยมจตุรัส
    triangle = (0.5 * x/3 * x/3) * 4 # สูตรสามเหลี่ยม
    ans = square - triangle

    return ans

if __name__ == '__main__' :
    main()

    
    
