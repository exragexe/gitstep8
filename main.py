

import string

user = input("Enter text: ")
user_title = user.title()

num = 0
num2 = 0
num3 = 0

try:
    print(user_title)  # 1 ex done
    for i in user:
        if i.isdigit():
            num += 1
    print(f"Кількість цифр у тексті: {num}")  # 2 ex done

    for h in user:
        if h in string.punctuation:
            num2 += 1
    print(f"Кількість розділових знаків у тексті: {num2}")  # 3 ex done

    for g in user:
        if g in "!":
            num3 += 1
    print(f"Кількість знаків оклику у тексті: {num3}")  # 4 ex done
except Exception as e:
    print(e)




