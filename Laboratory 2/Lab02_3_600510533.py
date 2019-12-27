#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 02
# Problem 3
# 204111 Sec 01A

print("First Equation")
m1 = float(input("Input m1: ")) #รับค่า m1
b1 = float(input("Input b1: ")) #รับค่า b1

print("Second Equation")
m2 = float(input("Input m2: ")) #รับค่า m2
b2 = float(input("Input b2: ")) #รับค่า b2

x = (b2-b1)/(m1-m2) #สมการหาค่า x 
y = m1*x + b1  #สมการหาค่า y

print("The point of intersection is at x = %.2f and y = %.2f " %(x,y))
