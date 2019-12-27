#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 2
# 204111 Sec 01A

def main():
    a = int(input()) # รับค่า
    b = int(input())
    c = int(input())
    ans = my_max_mid_min(a,b,c)
    print(ans) # แสดงผล

def my_max_mid_min(a,b,c):
    if a >= b >= c : # ถ้า a มากว่าหรือเท่ากับ b มากกว่าหรือเท่ากับ c 
        print("max = %d"%a) # แสดงค่ามากสุด = a
        print("mid = %d"%b) # แสดงค่าปานกลาง = b
        print("min = %d"%c) # แสดงค่าน้อยสุด = c
        
    elif a >= c >= b:
        print("max = %d"%a) # แสดงค่ามากสุด = a
        print("mid = %d"%c) # แสดงค่าปานกลาง = c 
        print("min = %d"%b) # แสดงค่าน้อยสุด = b
        
    elif b >= a >= c:
       print("max = %d"%b) # แสดงค่ามากสุด = b
       print("mid = %d"%a) # แสดงค่าปานกลาง = a
       print("min = %d"%c) # แสดงค่าน้อยสุด = c

    elif b >= c >= a:
       print("max = %d"%b) # แสดงค่ามากสุด = b
       print("mid = %d"%c) # แสดงค่าปานกลาง = c
       print("min = %d"%a) # แสดงค่าน้อยสุด = a

    elif c >= a >= b:
       print("max = %d"%c) # แสดงค่ามากสุด = c
       print("mid = %d"%a) # แสดงค่าปานกลาง = a
       print("min = %d"%b) # แสดงค่าน้อยสุด = b

    elif c >= b >= a:
       print("max = %d"%c) # แสดงค่ามากสุด = c
       print("mid = %d"%b) # แสดงค่าปานกลาง = b
       print("min = %d"%a) # แสดงค่าน้อยสุด = a

    


if __name__ == '__main__' :
    main()
        
        

