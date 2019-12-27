#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 4
# 204111 Sec 01A

def main():
    list_x = [[1, 2],
              [1, 2, 3],
              [1, 2],
              [1, 2],
              [1]]
    square_matrix(list_x)
    print(list_x)

def square_matrix(list_x):

    max_row = len(list_x) # หาจำนวนสูงสุดของแถวเพื่อเอามาลบจะได้ค่าที่ขาด

    max_col = 0
    for i in range(len(list_x)):
        if max_col < len(list_x[i]): # หาจำนวนสูงสุดของหลักเพื่อเอามาลบจะได้ค่าที่ขาด
            max_col = len(list_x[i])

    if max_row > max_col: # หาความยาวของด้านสีเหลี่ยม
        long_squ = max_row
    else:
        long_squ = max_col

    row_space = long_squ - len(list_x) # แถวว่างที่ใส่ 0 ลงไป
    for ar in range(row_space): # เพิ่ม 0 ในแถว list_x 
        list_x.append([0] * long_squ) # ใส่ 0 ลงไปในแถวที่ว่าง

    for i in range(len(list_x)): # เพิ่ม 0 ใส่แถว
        col_space = long_squ - len(list_x[i]) # หลักว่างที่ใส่ 0 ลงไป
        for ac in range(col_space): # เพิ่ม 0 ในหลัก list_x 
            list_x[i].append(0)


if __name__ == '__main__':
    main()
