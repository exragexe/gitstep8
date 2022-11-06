

try:
    num = int(input("Введіть число: "))
    first_num = num % 10
    res_first = num - first_num
    #1
    second_num = num % 100
    res_second = num - second_num
    #2
    third_num = num % 1000
    res_third = num - third_num
    #3
    fourth_num = num % 10000
    res_fourth = num - fourth_num
    #4

    for i in range(res_first, num+1):
        print(i, end=" ")
    print("")
    for h in range(res_second, num+1):
        if h %10 == 0:
            print(h, end=" ")
    print("")
    for g in range(res_third, num+1):
        if g % 100==0:
            print(g, end=" ")
    print("")
    for m in range(res_fourth, num+1):
        if m % 1000 == 0:
            print(m, end=" ")


except Exception as e:
    print(e)