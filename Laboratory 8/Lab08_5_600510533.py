#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 5
# 204111 Sec 01A

def main():
    num = int(input())
    ans = reverse_num(num)
    print(ans)

def reverse_num(num):
    return reverse_digits(num,0)

def reverse_digits(x,ans):
    if x == 0: # base case
        return ans
    return reverse_digits(x // 10, ans*10 + x % 10) # divide & conquer

if __name__ == '__main__':
    main()