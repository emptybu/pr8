total = 0

while True:
    user_input = input("Введите число или 'stop/end' для завершения: ")
    
    if user_input.lower() in ['stop', 'end']:
        break
    
    try:
        number = float(user_input)
        total += number
    except ValueError:
        print("Пожалуйста, введите корректное число.")

print(f"Сумма введенных чисел: {total}")
