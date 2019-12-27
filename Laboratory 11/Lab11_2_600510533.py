#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 2
# 204111 Sec 01A
import copy
def main():
    list_a = [[2, 3, 4, 5],
              [8, 7, 6, 5],
              [0, 1, 2, 3]]

    row = int(input())
    col = int(input())

    print(remove_row_col(list_a, row, col))

def remove_row_col(list_a, row, col):
    list_a = copy.deepcopy(list_a)
    if row >= -len(list_a) and row < len(list_a): # ถ้าอยู่ในขอบเขตให้ตัดจำนวณแถว
        list_a.pop(row)

    if col >= -len(list_a[0]) and col < len(list_a[0]): # ถ้าอยู่ในขอบเขตให้ตัดจำนวณคอลัม
        for r in range(len(list_a)):
            list_a[r].pop(col)

    return list_a
    
         

    
            



if __name__ == '__main__':
    main()
