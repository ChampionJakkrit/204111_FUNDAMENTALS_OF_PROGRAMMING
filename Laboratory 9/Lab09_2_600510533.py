#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 09
# Problem 2
# 204111 Sec 01A

def main():
    x = int(input())
    b = int(input())
    print(is_palindrome(x, b))

def is_palindrome(x, b):
    base = 0
    i = 0
    while x > 0: # เปลี่ยน x เป็นเลขฐาน b
        base += (x % b) * (10 ** i)
        i += 1
        x = x // b

    base = str(base) # เปลี่ยน int เป็น string
    reverse = base[len(base)-1::-1] # กลับเลข

    if reverse == base: # ถ้าเลขที่กลับเหมือนเลขฐานที่แปลงแล้ว
        return True 
    else:
        return False

    
if __name__ == '__main__':
    main()