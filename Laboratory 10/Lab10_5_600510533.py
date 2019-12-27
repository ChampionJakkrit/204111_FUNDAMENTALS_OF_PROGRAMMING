#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 10
# Problem 5
# 204111 Sec 01A

def main():
    num = int(input())
    print(num_to_word(num))


def three_digits_to_word(n):
    unit_list = ["", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen",
    "sixteen", "seventeen", "eighteen", "nineteen"]

    ten_list = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n == 0: # เลข 0
        return ("zero")

    elif n < 20: # ไม่เกิน 20
        return str(unit_list[n])

    elif 20 <= n < 100: # ระหว่าง 20-99
        ten_digits = n // 10
        units = n % 10
        if n % 10 == 0: # กรณีเป็น 0 (10,20,30,40,...)
            return str(ten_list[ten_digits])
        else: # กรณีไม่เป็น 0
            return str(ten_list[ten_digits] + "-" + unit_list[units])

    elif 100 <= n < 1000: # ระหว่าง 100-999
        hundred_digits = n // 100 # กรณีเป็นหลักร้อย (100,200,300,400,...)
        if (n % 100) < 20: # x(01-19) x = หลักร้อย
            two_units_of_hundred = n % 100
            return str(unit_list[hundred_digits] + " hundred "  + unit_list[two_units_of_hundred])
        else: # มากกว่า 20
            ten_digits = (n // 10) % 10
            units = n % 10
        if n % 10 == 0: # กรณีเป็น 0 (10,20,30,40,...)
            return str(unit_list[hundred_digits] + " hundred " + ten_list[ten_digits])
        else: # กรณีไม่เป็น 0
            return str(unit_list[hundred_digits] + " hundred " + ten_list[ten_digits] + "-" + unit_list[units])

def num_to_word(num):
    if num < 10 ** 3: # 0-999
        return three_digits_to_word(num)

    if 10 ** 3 <= num < 10 ** 6: # 1000-999,999
        three_units_of_thousand = num // 10 ** 3
        three_units_of_hundred = num % 10 ** 3
        # 1|000
        if three_units_of_hundred % 10 ** 3 == 0:
            return three_digits_to_word(three_units_of_thousand) + " thousand "
        # 1|001
        else:
            return three_digits_to_word(three_units_of_thousand) + " thousand " + three_digits_to_word(three_units_of_hundred)

    elif 10 ** 6 <= num < 10 ** 9: # 10**6-999,999,999
        three_units_of_million = num // 10 ** 6 # xxx|___|___
        three_units_of_thousand = (num // 10 ** 3) % 10 ** 3 # ___|xxx|___
        three_units_of_hundred = num % 10 ** 3 # ___|___|xxx

        # 1|001|000 กรณี 3 ตัวหลักร้อย = 0
        if three_units_of_thousand % 10 ** 3 != 0 and three_units_of_hundred % 10 ** 3 == 0 : 
            return three_digits_to_word(three_units_of_million) + " million " + three_digits_to_word(three_units_of_thousand) + " thousand "

        # 1|000|001 กรณี 3 ตัวหลักพัน = 0
        elif three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 != 0 : 
            return three_digits_to_word(three_units_of_million) + " million " + three_digits_to_word(three_units_of_hundred)

        # 1|000|000 กรณี 3 ตัวหลักพันและ 3 ตัวหลักร้อย = 0
        elif three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 == 0: 
            return three_digits_to_word(three_units_of_million) + " million "

        else: # 1|111|111 
            return three_digits_to_word(three_units_of_million) + " million " + three_digits_to_word(three_units_of_thousand) + " thousand " + three_digits_to_word(three_units_of_hundred)

    elif 10 ** 9 <= num < 10 ** 12:
        three_units_of_billion = num // 10 ** 9 # xxx|___|___|___
        three_units_of_million = (num // 10 ** 6) % 10 ** 3 # ___|xxx|___|___
        three_units_of_thousand = (num // 10 ** 3) % 10 ** 3 # ___|___|xxx|___
        three_units_of_hundred = num % 10 ** 3 # ___|___|___|xxx
        # 1|001|001|000
        if three_units_of_million % 10 ** 3 != 0 and three_units_of_thousand % 10 ** 3 != 0 and three_units_of_hundred % 10 ** 3 == 0:
            return three_digits_to_word(three_units_of_billion) + " billion " + three_digits_to_word(three_units_of_million) + " million " + three_digits_to_word(three_units_of_thousand) + " thousand "

        # 1|001|000|001
        elif three_units_of_million % 10 ** 3 != 0 and three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 != 0:
            return three_digits_to_word(three_units_of_billion) + " billion " + three_digits_to_word(three_units_of_million) + " million " + three_digits_to_word(three_units_of_hundred)

        # 1|001|000|000
        elif three_units_of_million % 10 ** 3 != 0 and three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 == 0:
            return three_digits_to_word(three_units_of_billion) + " billion " + three_digits_to_word(three_units_of_million) + " million "

        # 1|000|001|001
        elif three_units_of_million % 10 ** 3 == 0 and three_units_of_thousand % 10 ** 3 != 0 and three_units_of_hundred % 10 ** 3 != 0:
            return three_digits_to_word(three_units_of_billion) + " billion " +three_digits_to_word(three_units_of_thousand) + " thousand " + three_digits_to_word(three_units_of_hundred)

        # 1|000|000|001 
        elif three_units_of_million % 10 ** 3 == 0 and three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 != 0:
            return three_digits_to_word(three_units_of_billion) + " billion " + three_digits_to_word(three_units_of_hundred)

        # 1|000|000|000
        elif three_units_of_million % 10 ** 3 == 0 and three_units_of_thousand % 10 ** 3 == 0 and three_units_of_hundred % 10 ** 3 == 0:
            return three_digits_to_word(three_units_of_billion) + " billion "

        # 1|001|001|001
        else: 
            return three_digits_to_word(three_units_of_billion) + " billion " +three_digits_to_word(three_units_of_million) + " million " +three_digits_to_word(three_units_of_thousand) + " thousand " + three_digits_to_word(three_units_of_hundred)



if __name__ == '__main__':
    main()