try:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    # Приводим a и b к целым, чтобы определить границы
    a = int(a)
    b = int(b)

    if a > b:
        a, b = b, a

    for i in range(a + 1, b):
        print(i)
except ValueError:
    print("Пожалуйста, введите корректные вещественные числа.")
