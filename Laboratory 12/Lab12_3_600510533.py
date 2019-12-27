#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 3
# 204111 Sec 01A

def main():
    text = "He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."

    d = word_count(text)
    print(d)

def word_count(text):
    char_spec = "!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~"
    text_ = text.strip()
    text_ = text_.split()
    dict_text = dict()
    set_text = set()
    for key in text_: # สร้าง key ให้ไปอยู่ใน dict 
        low_text_set = key.strip(char_spec) # ตัดอักษรพิเศษที่อยู่หัวกับท้าย
        low_text_set = low_text_set.lower() # ทำให้เป็นตัวเล็ก

        set_text.add(low_text_set)

    for key in set_text: # ให้ value ตัวแรกเป็น 0 เพื่อบวกตัวซ้ำ
        dict_text[key] = 0

    for item in text_: # จองพื้นที่สรับให้ key มาอยู่
        low_text_dict = item.strip(char_spec) # ตัดอักษรพิเศษที่อยู่หัวกับท้าย
        low_text_dict = low_text_dict.lower() # ทำให้เป็นตัวเล็ก

        dict_text[low_text_dict] += 1 # เอาแต่ละตัวไปใส่ใน dict

    return dict_text

if __name__ == '__main__':
    main()