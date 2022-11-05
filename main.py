

try:
    num = input("Введіть список чисел: ")
    num_sp = num.split(" ")
    res = [float(i) for i in num_sp]


    print(f"Сумма чисел = {float(sum(res))} \n AVG = {float(sum(res) / len(num_sp))}")
except Exception as e:
    print(e)