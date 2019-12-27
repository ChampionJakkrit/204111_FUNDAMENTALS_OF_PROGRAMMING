def main():
    x = float(input())
    ans = float_to_bin(x)
    print("%.6f"%ans)
    
def float_to_bin(x):
    if x < 0:
        return -1*(float_to_bin(-x))

    int_of_x = int(x)
    ans1 = 0
    i = 0
    while int_of_x != 0:
        ans1 += (int_of_x % 2)*(10 ** i)
        i += 1
        int_of_x = int_of_x // 2

    float_of_x = float(x) - int(x)
    ans2 = 0
    i = 5
    while i >= 0:
        float_of_x *= 2
        ans2 += int(float_of_x)*(10 ** i)
        i -= 1
        float_of_x = float_of_x - int(float_of_x)

    return ans1 + (ans2/(10**6))



if __name__ == '__main__':
    main()
