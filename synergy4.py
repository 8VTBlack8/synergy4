def calculate_result():
    # запрашиваем данные
    number = input("Введите пятизначное, целое число: ")

    # проверка на 5ти значность
    if len(number) != 5 or not number.isdigit():
        print("Ошибка, введите корректное пятизначное, целое число.")
        return

    # преобразование строки
    number = int(number)

    # извлечение
    ten_thousands = number // 10000 % 10
    thousands = number // 1000 % 10
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    units = number % 10

    
    difference = ten_thousands - thousands

    # проверка деления на 0
    if difference == 0:
        print("Ошибка: деление на  ноль.Разность между десятками тысяч и тысячами равна нулю.")
        return

    # вычисляем
    result = (tens ** units) * hundreds / difference

    # ну и результат
    print(f"Результат: {result}")

calculate_result()

