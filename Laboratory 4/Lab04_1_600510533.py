#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 1
# 204111 Sec 01A

def main():
    first = int(input()) # รับค่า
    second = int(input())
    ans = love6(first,second)
    print(ans) # แสดงผล
    
def love6(first,second):
    if first == 6 or second == 6: # ถ้าตัวใดตัวหนึ่ง = 6 ให้แสดง True
        return True
    
    elif first + second == 6:  # ถ้าทั้งสองจำนวน + กัน = 6 ให้แสดง True
        return True
    
    elif abs(first - second) == 6:  # ถ้าสองจำนวน - กัน = 6 ให้แสดง True
        return True
 
    else :
        return False # มิเช่นนั้นแสดง False

if __name__ == '__main__' :
    main()
