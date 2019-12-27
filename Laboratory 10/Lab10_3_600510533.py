#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 10
# Problem 3
# 204111 Sec 01A

def main():
    list_a = [1, 2, 3, 4]
    n = int(input()) # รับค่า
    print(nondest_rotate_list(list_a, n))

def nondest_rotate_list(list_a, n):
    new_list = list_a[:] # สร้าง list ใหม่ของ list_a (เพื่อไม่ทำลาย list เดิม)
    for item in range(n % len(new_list)): # วนตาม n %len(new_list) รอบ
        out = new_list.pop(-1) # เอาตัวสุดท้ายมาเก็บไว้
        new_list.insert(0, out) # เอาตัวที่เก็บไว้มาใส่ตน.ที่ 0

    return new_list
        

        


if __name__ == '__main__':
    main()

