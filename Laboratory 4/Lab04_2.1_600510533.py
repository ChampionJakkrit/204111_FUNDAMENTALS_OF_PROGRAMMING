# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 04
# Problem 2
# 204111 Sec 01A

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_max_mid_min(a, b, c)

def my_max_mid_min(a, b, c):
    max_ = a
    if a < b:
        max_ = b
    if a < c:
        max_ = c

    min_ = a
    if a > b:
        min_ = b
    if a > c:
        min_ = c

    all_ = a + b + c
    mid_ = all_ - max_ - min_

    print("max = %d"%max_)
    print("mid = %d"%mid_)
    print("min = %d"%min_)

    
        

if __name__ == '__main__':
    main()