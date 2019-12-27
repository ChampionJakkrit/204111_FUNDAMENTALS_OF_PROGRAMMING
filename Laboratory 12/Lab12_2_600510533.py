#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 2
# 204111 Sec 01A

def main():
    set_a = {'a', 'b','c'}

    print(power_set(set_a))

def power_set(set_a) : # เอา list มาทำเป็น set
    set_a = powset2(list(set_a))
    for i in range(len(set_a)) :
        set_a[i] = set(set_a[i])
    return set_a

def powset2(seq): # ทำเป็น list 
    result = []
    if seq:
        head, tail = seq[:1], seq[1:]
        for smaller in powset2(tail):
            result.append(smaller)
            result.append(head + smaller)
    else:
        result.append([])
    return result

if __name__ == '__main__':
    main()