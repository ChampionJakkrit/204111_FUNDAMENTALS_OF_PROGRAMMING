#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 05
# Problem 4
# 204111 Sec 01A

def main():
    l1, t1, w1, h1 = map(int, input().split())
    l2, t2, w2, h2 = map(int, input().split())
    ans = is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2)
    print(ans)

def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):
           #    กรณี แกน x                                     กรณี แกน y
    if (l1  <= l2 + w2 and l2 <= l1 + w1) and (t1 <= t2 + h2 and t1 + h1 >= t2):
    # (ขอบซ้ายของสี่เหลี่ยมอันที่ 1 <= ขอบขวาสี่เหลี่ยมอันที่ 2 และ ขอบซ้ายของสี่เหลี่ยมอันที่ 2 <= ขอบขวาสี่เหลี่ยมอันที่ 1) และ
    # (ขอบบนสี่เหลี่ยมอันที่ 1 <= ขอบล่างสี่เหลี่ยมอันที่ 2 และ ขอบล่างสี่เหลี่ยมอันที่ 1 >= ขอบล่างสี่เหลี่ยมอันที่ 2)
        return True
    else:
        return False



if __name__ == '__main__':
    main()