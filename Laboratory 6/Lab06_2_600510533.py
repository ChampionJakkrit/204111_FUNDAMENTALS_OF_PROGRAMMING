#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 06
# Problem 2
# 204111 Sec 01A

import math


def main():
  x = float(input()) # รับค่า
  ans = float_to_bin(x)
  print("%.6f" % ans) # แสดงผล


def float_to_bin(x):
  x_old = x
  x = abs(x)
  ans = 0
  i = 0
  integer = int(x)
  float_6 = x - integer
  while integer != 0:
    ans = ((integer % 2) * (10 ** i)) + ans
    i += 1
    integer = integer // 2

  a = 0
  for j in range(0, 6, 1):
    float_6 = float_6 * 2
    f = int(float_6)
    a = a + (f * (10 ** (6 - j - 1)))
    float_6 -= f

  last = a / 1000000
  front = ans

  res =  front + last

  if x_old < 0 :
    res *= -1

  return res


if __name__ == '__main__':
    main()
 