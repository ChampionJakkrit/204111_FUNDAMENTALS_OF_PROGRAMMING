#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 1
# 204111 Sec 01A

def main():
    square_frame(3,".")


def square_frame(n, sep=' '):
    for i in range(n):
        for j in range(n):
            if i == 0: # ขอบบน
                print("%02d"%(j+1),end="") 
            elif j == n-1: # ขอบขวา
                print("%02d"%(i+n),end="")
            elif j == 0: # ขอบซ้าย
                print("%02d"%(4*n-4-i+1),end="")
            elif i == n-1: # ขอบล่าง
                print("%02d"%((3*n-2)-j),end="")
            
            else:
                print("%c%c"%(sep,sep),end="")

            if j != n-1:
                print(sep,end="")


            
            # print(i,j, " ",end = "")
        print("")


if __name__ == '__main__':
    main()


