#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 08
# Problem 3
# 204111 Sec 01A

def main():
    n = int(input())
    ans = is_prime(n)
    print(ans)

def is_prime(n):
    return prime(n,2)

def prime(n,c):
    if n % c == 0: # base case
        return False
    elif n**0.5 < c: # divide & conquer
        return True
    
    return prime(n,c+1) # combine


if __name__ == '__main__':
    main()
