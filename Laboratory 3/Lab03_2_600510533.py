#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 2
# 204111 Sec 01A

def main():
    x = int(input()) # รับค่าจากผู้ใช้
    number = reverse_digits(x)
    print("%04d" %number) # แสดงค่า

def reverse_digits(x):
    number1 = (x % 10) # เก็บค่าตัวที่ 1
    number2 = (x % 100)//10 # เก็บค่าตัวที่ 2
    number3 = (x % 1000)//100 # เก็บค่าตัวที่ 3
    number4 = (x % 10000)//1000 # เก็บค่าตัวที่  4
    
                     
    # นำค่าที่ได้มาบวกกัน
    return  number1 * 1000 +  number2 * 100 +  number3 * 10 +  number4
 

if __name__ == '__main__' :
    main()







    

    
