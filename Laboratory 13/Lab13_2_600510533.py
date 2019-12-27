#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 13
# Problem 2
# 204111 Sec 01A

def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
              ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
              ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
              ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
              ("9/11/2042", "Event I")]
    event = search_event(list_x, "29/02/2032")
    print("---")
    print(event)

def search_event(list_x, key):
  
  key = key.split("/") # กรณี 02 เป็น 2
  for i in range(3):
    key[i] = str(int(key[i])) # ทำเป็น int(02) แล้วทำเป็น str(2) แสดงว่า 02 = 2

  filter_ = ""
  for i in range(3):
    filter_ += key[i]
    if i < 2: # หาแค่วันกับเดือน
      filter_ += '/'
  key = filter_ # เป็นปีก็ให้เท่าเดิม

  for k, v in list_x: # หา value ให้จับกับ key 
      if (k == key) :
          return (k, v)
  return None # หาไม่เจอ คืนค่า None

if __name__ == '__main__':
    main()
