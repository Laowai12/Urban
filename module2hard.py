def find_password(number):
    pairs = []
    for i in range(1, 20):
        for j in range(i + 1, 20):
            if (i + j) != number:
                continue
            pairs.append((i, j))

    result = ''.join([str(pair[0]) + str(pair[1]) for pair in pairs])
    return result


number = int(input("Введите число от 3 до 20: "))
if 3 <= number <= 20:
    password = find_password(number)
    print(f"Для числа {number} нужный пароль: {password}")
else:
    print("Число должно быть от 3 до 20")
