def calculate_result():
    # ����������� ������
    number = input("������� ����������� ����� �����: ")

    # �������� ����� 5�� �������� �����
    if len(number) != 5 or not number.isdigit():
        print("����������, ������� ���������� ����������� ����� �����.")
        return

    # ��������� ������ � �����
    number = int(number)

    # ����������� �����
    ten_thousands = number // 10000 % 10
    thousands = number // 1000 % 10
    hundreds = number // 100 % 10
    tens = number // 10 % 10
    units = number % 10

    
    difference = ten_thousands - thousands

    # �������� �� �������
    if difference == 0:
        print("������: ������� �� ����.")
        return


    result = (tens ** units) * hundreds / difference

    # ������� ���������
    print(f"���������: {result}")

calculate_result()

