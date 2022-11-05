


try:
    numbers = input("Ведіть список чисел:")
    fnum = input("Введіть число яке ви шукаєте:")
    num = 0

    if fnum not in numbers:
        print(f"{fnum} not in text")

    res = numbers.count(fnum)



    print(f"Кількість {fnum} в тексті - {res}")

except Exception as e:
    print(e)