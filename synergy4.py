def calculate_result():
    # запрашиваем данные
    number = input("Введите пятизначное целое число: ")

    # проверка ввода 5ти значного числа
    if len(number) != 5 or not number.isdigit():
        print("Пожалуйста, введите корректное пятизначное целое число.")
        return

    # переводим строку в число
    number = int(number)

    # выдергиваем цифры
    ten_thousands = number // 10000 % 10
    thousands = number // 1000 % 10
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    units = number % 10

    
    difference = ten_thousands - thousands

    # проверка на деление
    if difference == 0:
        print("Ошибка: Деление на ноль.")
        return


    result = (tens ** units) * hundreds / difference

    # выводим результат
    print(f"Результат: {result}")

calculate_result()

