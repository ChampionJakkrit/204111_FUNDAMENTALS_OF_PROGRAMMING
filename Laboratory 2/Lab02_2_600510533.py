#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 02
# Problem 2
# 204111 Sec 01A

h = float(input("Input height (m): ")) #รับข้อมูลความสูง
w = float(input("Input weight (kg): ")) #รับข้อมูลน้ำหนัก
BMI = w / (h**2) #สูตรดัชนีมวลกาย
print("BMI is %.4f" %BMI)
