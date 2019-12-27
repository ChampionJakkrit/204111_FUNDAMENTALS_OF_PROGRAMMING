#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 10
# Problem 2
# 204111 Sec 01A

def main():
    print(classify([10, 'hello', 23.5, 4]))


def classify(list_x):
    list_a = []
    list_b = []
    list_c = []

    for item in list_x: # หาแต่ละตัวใน list_x
        if isinstance(item, int): # ถ้าเป็น int ให้ทำเป็น list ใน list_a
            list_a.append(item)
        elif isinstance(item, float):  # ถ้าเป็น float ให้ทำเป็น list ใน list_b
            list_b.append(item)
        elif isinstance(item, str):  # ถ้าเป็น str ให้ทำเป็น list ใน list_c
            list_c.append(item) 

    return (list_a , list_b , list_c)



if __name__ == '__main__':
    main()