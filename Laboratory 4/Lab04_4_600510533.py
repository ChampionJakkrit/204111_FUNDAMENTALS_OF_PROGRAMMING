#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 4
# 204111 Sec 01A

def main():
    x = float(input()) # รับค่า
    ans = round_to_int(x)
    print(ans) # แสดงผล

def round_to_int(x):
    if x >= 0: # x มากกว่าหรือเท่ากับ 0
        if x % 1 >= 0.5: # นำ x ไปหาเศษเหลือ ถ้ามากกว่าหรือเท่ากับ 0.5 ให้คืนค่า x + 1
            return int(x) + 1
        else : # นำ x ไปหาเศษเหลือ ถ้าน้อยกว่าหรือเท่ากับ 0.5 ให้คืนค่า x 
            return int(x)
        
    else:  # x น้อยกว่าหรือเท่ากับ 0
        if abs(x) % 1 < 0.5: # นำ x ไปหาเศษเหลือ ถ้าน้อยกว่า 0.5 ให้คืนค่า x 
            return int(x)
        else : # นำ x ไปหาเศษเหลือ ถ้ามากกว่า 0.5 ให้คืนค่า x - 1
            return int(x) - 1

if __name__ == '__main__' :
    main()

    
    
