#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 2
# 204111 Sec 01A

def main():
    n = int(input())
    num = int(input())
    ans = n_base_to_10(n, num)
    print(ans)

def n_base_to_10(n, num):
    ans = base(n,num,0)
    return ans
   
def base(n,num,i):
    ans = -1
    if num == 0: # base case
        return 0
    return base(n,num//10,i+1) + (num%10) * n**i # divide & conquer


if __name__ == '__main__':
    main()