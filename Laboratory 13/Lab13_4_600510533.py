#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 13
# Problem 4
# 204111 Sec 01A

def main(): 

    print(polynomial_addition([(2, 6), (1, 34), (0, -8)], [(2, -6), (0, 2), (1, 1)]))

def polynomial_addition(p1, p2):
    dict_p = dict()
    p3 = p1 + p2 # lsit รวม
    for key in p3:
        dict_p[key[0]] = 0

    for i in range(len(p3)):
        power = p3[i][0] # เลขยกกำลัง
        num = p3[i][1] # เลขสัมประสิทธิ์
        dict_p[power] += num # บวกสัมประสิทะิ์กำลังนั้นๆ

    list_tuple = [] 
    for key in dict_p: # ทำเป็น tuple
        l = (key,dict_p[key])
        if dict_p[key] != 0:
            list_tuple.append(l)

    list_tuple.sort()

    return list_tuple[::-1]

if __name__ == '__main__':
    main()