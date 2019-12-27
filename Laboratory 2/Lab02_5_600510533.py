#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 02
# Problem 5
# 204111 Sec 01A

n = int(input("Enter n: "))  # รับค่า
fi = (((1 + 5 ** 0.5) / 2) ** n) / 5 ** 0.5 + 0.5  # สูตรบิเนห์
print("fib(%d) = %d" % (n, fi))
