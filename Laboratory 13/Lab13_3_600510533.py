#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 13
# Problem 3
# 204111 Sec 01A

def main():
    n = int(input())
    print(prime_factor(n))
    print(coprime_factor(180, 48))


def prime_factor(n):

    list_n = []
    i = 2
    while i <= int(n**0.5):
        while n % i == 0 : # แสดงตัวประกอบของจำนวนของ x
            n //= i 
            list_n.append(i)
        i += 1
    if n != 1:
        list_n.append(n)
    return list_n

def coprime_factor(a, b):

    while b > 0: # หา หรม. จาก ตัวที่หาร a กับ b มากสุดก่อน
        r = a % b
        a = b
        b = r
    
    ans = prime_factor(a) # แล้วเอาหรม.นั้นไปหาจำนวณประกอบ นั่นคือคำตอบ
    return ans


if __name__ == '__main__':
    main()
