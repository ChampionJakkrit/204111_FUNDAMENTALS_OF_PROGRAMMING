#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 3
# 204111 Sec 01A

def main():
    p = int(input())
    c = int(input())
    ans = calculate_p2p_evolve_exp(p,c)
    print(ans)

def calculate_p2p_evolve_exp(p,c):
    if p <= c//12: # ลูกอมมากกว่านก
        return p * 500
    else: # ลูกอมน้อยกว่านก
        return ((c+(p-1))//12)*500 # นกที่จะใช้ transfer ต่อไป
        
       


if __name__ == '__main__' :
    main()
