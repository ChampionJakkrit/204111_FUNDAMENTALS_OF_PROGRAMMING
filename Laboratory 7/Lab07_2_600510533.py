#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 2
# 204111 Sec 01A

def main():
    x = int(input())
    y = int(input()) # เปลี่ยนจำนวนฐาน
    ans = digit_count(x, y)
    print(ans)

def digit_count(x, base=10):
    x = abs(x)
    i = 0

    #หาจำนวนครั้งในการหาร
    while x != 0: 
        i += 1
        x = x // base
    return i 

    

if __name__ == '__main__':
    main()