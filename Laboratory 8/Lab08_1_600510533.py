#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 1
# 204111 Sec 01A

def main():
    x = int(input())
    y = int(input())
    ans = gcd(x, y)
    print(ans)

def gcd(x, y):
    if y == 0: # base case
        return x
    return gcd(y, x % y) # divide & conquer

if __name__ == '__main__':
    main()