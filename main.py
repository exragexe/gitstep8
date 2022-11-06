

import random

try:
    minus = []
    plus = []
    zero = []
    numbers = [-5, 1, 12, 55, -44, -101, 89, 44, 66, 0, -124, -63, -23, 0, 0]
    random.shuffle(numbers)
    print(f"{numbers} \n Максимальне число - {max(numbers)} \n Мінімальне число - {min(numbers)}")

    for i in numbers:
        if i < 0:
            minus.append(i)
        if i > 0:
            plus.append(i)
        if i == 0:
            zero.append(i)

    print(f" Кількість від'ємних значень - {len(minus)} \n Кількість додатніх значень - {len(plus)}\n Кількість нулів - {len(zero)}")

except Exception as e:
    print(e)