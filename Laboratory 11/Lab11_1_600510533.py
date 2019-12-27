#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 1
# 204111 Sec 01A
def main():
    m1 = [[1, 2, 3],
          [4, 5, 6]]
    m2 = [[7, 8],
         [9, 10],
         [11,12]]
    ans = matrix_mult(m1, m2)
    print(ans)

def matrix_mult(m1, m2):
    rows_m1 = len(m1) # i ของ m1
    cols_m1 = len(m1[0]) # j ของ m1
    rows_m2 = len(m2) # i ของ m2
    cols_m2 = len(m2[0]) # j ของ m2
    a = []
    for row in range(rows_m1): # สร้าง zero matrix
        a += [[0] * cols_m2] 
    
    if cols_m1 != rows_m2:
        return None
    else:
        for i in range(rows_m1):
            for j in range(cols_m2):
                for k in range(cols_m1): # สร้าง k มาวิ่งตัวคูณที่เปลี่ยนไป
                    a[i][j] += m1[i][k] * m2[k][j]
    return a

if __name__ == '__main__':
    main()