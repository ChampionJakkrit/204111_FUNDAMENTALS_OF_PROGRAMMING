#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 07
# Problem 
# 204111 Sec 01A

def main():
    n = int(input())
    ans = pyramid_stairs(n)


def pyramid_stairs(n):
    if n == 0:
        print("")
        return 
    for i in range(3*n):
        n_spac = (n - ((i+3)//3))*5
        for j in range(n_spac):
            print(" ", end = '')
        if i % 3 == 0:
            print("  o  ",end = '')
            print("******",end = '')
            for s in range(((i+2)//3)*10):
                print(" ",end = '')

            print("******",end = '')
            print("  o",end = '')
        elif i % 3 == 1:
            print(" /|\\ ",end = '')
            print("*",end = '')
            for s in range(((i+2)//3)*10):
                print(" ",end = '')

            print("*", end = '')
            print(" /|\\",end = '')
     
        elif i % 3 == 2:
            print(" / \\ ",end = '')
            print("*",end = '')
            for s in range(((i+2)//3)*10):
                print(" ",end = '')
            
            print("*",end = '')
            print(" / \\",end = '')
        print("")

    for l in range(n*(10)+12):
        print("*",end = '')


if __name__ == '__main__':
    main()
