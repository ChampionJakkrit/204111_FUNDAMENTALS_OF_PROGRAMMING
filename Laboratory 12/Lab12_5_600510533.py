#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 5
# 204111 Sec 01A

import string
def main():
    list_x = ['beer', 'wine', 'vinegar', 'vodka']
    radix_word(list_x, True)
    print('--------')
    print(list_x)


def radix_word(list_x, show_step=False):
    max_word = 0
    for i in range(len(list_x)): # หาความยามที่สุดของคำใน list_x
        if max_word < len(list_x[i]):
            max_word = len(list_x[i])

    lower_case = string.ascii_lowercase # สร้างตัวพิมพ์เล็กทั้งหมด
    dict_space = dict()
    
    for j in range(max_word-1,-1,-1): # นับหลักจาดสุดท้ายมาหน้าสุด
        for i in range(26):
            dict_space[lower_case[i]] = list()
        dict_space[" "] = list()

        for i in range(len(list_x)):
            last_index_of_list_xi = len(list_x[i])-1
            if (last_index_of_list_xi >= j):
                traget = list_x[i][j]
            else:
                traget = " " # เป้าหมายที่จะเอาตัวอักษรไปลง
            dict_space[traget].append(list_x[i])

        # clear all element
        while (len(list_x) > 0):
            list_x.pop()

        for i in range(len(dict_space[" "])):
            list_x.append(dict_space[" "][i])

        for mem in lower_case:
            for i in range(len(dict_space[mem])):
                list_x.append(dict_space[mem][i])

        if show_step == True:
            print(list_x)


        

    

if __name__ == '__main__':
    main()