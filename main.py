

try:

    def viraz():
        user = input("Введіть арифметичний вираз. Приклад(12 + 7): ")

        user_sp = user.split(" ")
        res = [float(i) for i in user_sp[0::2]]

        if len(user_sp) > 3:
            return "Error. Вираз може складатися тільки з трьох частин: число, операція, число"
        elif "+" in user_sp:
            return f"Сума виразу дорівнює - {res[0] + res[1]}"
        elif "-" in user_sp:
            return f"Різниця виразу дорівнює - {res[0] - res[1]}"
        elif "*" in user_sp:
            return f"Добуток виразу дорівнює - {res[0] * res[1]}"
        elif "/" in user_sp:
            return f"Ділення виразу дорівнює - {res[0] / res[1]}"
        else:
            return "Error. Можливі операції: +, -, *, /."

    print(viraz())


except Exception as ex:
    print(ex)
