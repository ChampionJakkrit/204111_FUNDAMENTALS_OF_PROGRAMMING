#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 05
# Problem 2
# 204111 Sec 01A


def main():
    a, b, c = map(int, input().split())
    ans = is_p_triple(a, b, c)
    print(ans)


def is_p_triple(a, b, c):

    max_, mid_, min_ = max_mid_min(a, b, c)
    c = (mid_ ** 2 + min_ ** 2) ** 0.5  # Pythagorean triple
    if c == max_:  # ถ้า c เท่ากับค่าสูงสุดให้คืนค่า True

        return True

    else:  # ถ้า c ไม่เท่ากับค่าสูงสุดให้คืนค่า False

        return False


def max_mid_min(a, b, c):  # หาค่าสูงสุด
    if a >= b >= c:
        return (a, b, c)

    elif a >= c >= b:
        return (a, c, b)

    elif b >= a >= c:
        return (b, a, c)

    elif b >= c >= a:
        return (b, c, a)

    elif c >= a >= b:
        return (c, a, b)

    elif c >= b >= a:
        return (c, b, a)


if __name__ == '__main__':
    main()
