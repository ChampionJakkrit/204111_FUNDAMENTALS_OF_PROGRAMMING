#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 10
# Problem 4
# 204111 Sec 01A

def main():
    list_a = [1, 2, 3, 4]
    n = int(input()) # รับค่า
    print(dest_rotate_list(list_a, n))

def dest_rotate_list(list_a, n):
    for item in range(n % len(list_a)): # วนตาม n %len(new_list) รอบ
        out = list_a.pop(-1) # เอาตัวสุดท้ายมาเก็บไว้
        list_a.insert(0, out) # เอาตัวที่เก็บไว้มาใส่ตน.ที่ 0

if __name__ == '__main__':
    main()