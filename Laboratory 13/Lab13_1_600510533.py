#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 13
# Problem 1
# 204111 Sec 01A

def main():
    list_x = ["11/1/2100", "5/12/1999", "19/1/2003", "11/9/2001"]
    sort_date(list_x)
    print("---")
    print(list_x)

def sort_date(list_x):
    
    all_element = len(list_x)
    for i in range(all_element): # ทำ str เป็น Tuple เพื่อเอา Tuple ไป sort
        s = list_x[i].split("/")
        s = list(reversed(s)) # กลับเพื่อเทียบ ปี ก่อน
        for j in range(3):
            s[j] = int(s[j])
        s = tuple(s) 
        list_x[i] = s
    list_x.sort()

    for i in range(all_element): # ทำกลับ
        s = list(list_x[i])
        s = list(reversed(s))
        for j in range(3):
            s[j] = str(s[j]) # ทำเป็น str
        m = ""
        for j in range(3):
            m += s[j]
            if j < 2:
                m += '/'

        list_x[i] = m


if __name__ == '__main__':
    main()