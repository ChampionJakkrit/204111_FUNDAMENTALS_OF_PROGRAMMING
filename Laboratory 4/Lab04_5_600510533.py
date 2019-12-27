#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 5
# 204111 Sec 01A

def main():
    x = float(input()) # รับค่า
    ans = nearest_odd(x)
    print(ans) # แสดงผล

def nearest_odd(x):
    if x >= 0: # x มากกว่าหรือเท่ากับ 0 (ค่าบวก)
        if int(x) % 2 == 0: # ถ้า x เป็นเลขคู่ ให้คืนค่า x + 1
            return int(x) + 1
        else : # ถ้า x เป็นเลขคี่ ให้คืนค่า x
            return int(x)
        
    else: # x น้อยกว่าหรือเท่ากับ 0 (ค่าลบ)
        if abs(int(x)) % 2 == 0:  # x เป็นเลขคู่
            if x % 1 != 0: # ถ้า x ไม่เท่ากับ 0 ให้คืนค่า x - 1 (ไม่เป็นจำนวนเต็ม = ลบทศนิยม)
                return int(x) - 1
            else:  # ถ้า x เท่ากับ 0 ให้คืนค่า x + 1 (เป็นลบจำนวนเต็ม)
                return int(x) + 1
        else:  # ถ้า x เป็นเลขคี่ ให้คืนค่า x
             return int(x)



if __name__ == '__main__' :
    main()

        
