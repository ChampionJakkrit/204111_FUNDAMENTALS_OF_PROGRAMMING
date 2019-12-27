#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 4
# 204111 Sec 01A

def main():
    list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]

    print(sum_nested_list(list_a))

def sum_nested_list(list_a):
    keep = 0
    if isinstance(list_a,list): # เช็คว่าเป็น list มั้ย
        for i in list_a: # วนหาเลขที่อยู่ใน list_a 
            sum_ = sum_nested_list(i) # แต่ในการวนจะเจอ list ซ้อนอีกที ให้ทำเหมือนเดิมซ้อนกันไปเรื่อยๆ
            keep += sum_ # บวก เลขที่อยู่ในลิสทั้งหมด
        return keep
    else:
        return list_a # ถ้าไม่ใช่ list ก็เคือเป็นตัวเลข ให้รีเทิร์นกลับไปเลย

if __name__ == '__main__':
    main()
