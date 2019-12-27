#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 1
# 204111 Sec 01A

def main():
    list_a = [(2, 7, 1.5), # a
              (3.2, 2.5, 4.06), # b
              (-5.5, -4.5, 2.5), # c
              (2, -5.2, 3), # d
              (7.2, -2.8, 1.2)] # e

    print(count_segment(list_a))

def count_segment(list_a):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for i in list_a:
        x = i[0]
        y = i[1]
        r = i[2]
        if (x >= 0 and y >= 0): # q1
            if x - r < 0:
                q2 += 1
            if y - r < 0:
                q4 += 1
            if (x**2 + y**2)**0.5 - r < 0:
                q3 += 1
            q1 += 1
        elif (x <= 0 and y >= 0): # q2
            if x + r > 0:
                q1 += 1
            if y - r < 0:
                q3 += 1
            if (x**2 + y**2)**0.5 - r < 0:
                q4 += 1
            q2 += 1
        elif (x <= 0 and y <= 0): # q3
            if x + r > 0:
                q4 += 1
            if y + r > 0:
                q2 += 1
            if (x**2 + y**2)**0.5 - r < 0:
                q1 += 1
            q3 += 1
        else: # q4
            if x - r < 0:
                q3 += 1
            if y + r > 0:
                q1 += 1
            if (x**2 + y**2)**0.5 - r < 0:
                q2 += 1
            q4 += 1
    return (q1 , q2 , q3, q4)


if __name__ == '__main__':
    main()