#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 05
# Problem 1
# 204111 Sec 01A


def main():
    x1, y1, r1 = map(float, input().split())  # รับค่า
    x2, y2, r2 = map(float, input().split())
    ans = intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6)  # แสดงผล
    print(ans)


def intersects(x1, y1, r1, x2, y2, r2, epsilon=10 ** -6):
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

    if (r1 + r2) > distance:  # ถ้ารัศมี > ระยะทาง
        # ถ้ารัศมี - ระยะทาง > 10 ** -6 คืนค่า 1
        if (r1 + r2) - distance > epsilon:
            return 1

    # ถ้ารัศมี - ระยะทาง = 0 (0 เท่ากันแต่ epsilon ทศนิยมมากกว่า) คืนค่า 0
    if abs((r1 + r2) - distance) < epsilon:
        return 0

    else:  # ถ้ารัศมี < ระยะทาง คืนค่า -1
        return -1


if __name__ == '__main__':
    main()
