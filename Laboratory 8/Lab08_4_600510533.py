#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 4
# 204111 Sec 01A

def main():
    n = int(input())
    ans = series(n)
    print(ans)

def series(n):
    if n == 0: # basecase
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return series(n-1) + 2*series(n-2) # divide & conquer

if __name__ == '__main__':
    main()