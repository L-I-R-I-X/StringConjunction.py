# Инициализация переменных
SIZE = 8
str1 = [''] * (SIZE + 1)  # Символьный массив для первой строки
str2 = [''] * (SIZE + 1)  # Символьный массив для второй строки
result = [''] * (SIZE + 1)  # Символьный массив для результата

# Ввод первой строки
temp1 = input()

# Проверка длины первой строки
if len(temp1) > SIZE:
    print("Строка не должна превышать 8 символов!")
    exit(1)

# Проверка символов первой строки
for char in temp1:
    if char != '0' and char != '1':
        print("Строка должна содержать только '0' и '1'.")
        exit(1)

# Дополнение первой строки нулями
zeros_to_add = SIZE - len(temp1)
for i in range(zeros_to_add):
    str1[i] = '0'

for i in range(zeros_to_add, SIZE):
    str1[i] = temp1[i - zeros_to_add]

str1[SIZE] = '\0'  # Добавление завершающего нуля

# Ввод второй строки
temp2 = input()

# Проверка длины второй строки
if len(temp2) > SIZE:
    print("Строка не должна превышать 8 символов!")
    exit(1)

# Проверка символов второй строки
for char in temp2:
    if char != '0' and char != '1':
        print("Строка должна содержать только '0' и '1'.")
        exit(1)

# Дополнение второй строки нулями
zeros_to_add = SIZE - len(temp2)
for i in range(zeros_to_add):
    str2[i] = '0'

for i in range(zeros_to_add, SIZE):
    str2[i] = temp2[i - zeros_to_add]

str2[SIZE] = '\0'  # Добавление завершающего нуля

# Конъюнкция битовых строк
for i in range(SIZE):
    result[i] = '1' if (str1[i] == '1' and str2[i] == '1') else '0'

result[SIZE] = '\0'  # Добавление завершающего нуля

# Вывод результатов
print("Первая строка (с нулями):", ''.join(str1[:SIZE]))
print("Вторая строка (с нулями):", ''.join(str2[:SIZE]))
print("Результат:", ''.join(result[:SIZE]))