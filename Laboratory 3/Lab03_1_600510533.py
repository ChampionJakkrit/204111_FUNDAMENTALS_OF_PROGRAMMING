#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 03
# Problem 1
# 204111 Sec 01A
import math


def main():
    surface_area = float(input("input surface area: ")) # รับค่าจากผู้ใช้งาน
    radius = find_r_from_surface_area(surface_area) # หารัศมีจากพื้นที่ผิว
    volume =sphere_volume(radius) # หาปริมาตรจากรัศมี
    print("volume = %.2f"%(volume)) #แสดงค่า

def find_r_from_surface_area(surface_area):
    # surface area  4*PI*r**2
    # r = sqrt(surface/(4PI))
    radius = math.sqrt(surface_area/(4*math.pi)) # สูตรหารัศมี

    return radius

def sphere_volume(radius):
    # volume =4/3*PI*r**3
    volume =(4/3)*math.pi*(radius**3) # สูตรหาปริมาตร

    return volume


if __name__ == '__main__' :
    main()

