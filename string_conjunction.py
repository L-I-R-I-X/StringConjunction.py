SIZE = 8

inPromptTemplate = "Введите {N}-ую строку\n"
outPromptTemplate = "{N}-ая строка (с нулями)"
outPromptRes = "Результат"

def input_string(n: int) -> str:
    prompt = inPromptTemplate.format(N=n)
    print(prompt, end="")
    return input()

def check_string(str_to_check: str) -> bool:
    if len(str_to_check) > SIZE:
        print(f"Длина строки не должна превышать {SIZE} символов!\n")
        return False
    for char in str_to_check:
        if char not in ('0', '1'):
            print("Строка должна содержать только '0' и '1'.\n")
            return False
    return True

def add_zeros(str_to_pad: str) -> str:
    if len(str_to_pad) < SIZE:
        print(f"Длина строки менее {SIZE} символов")
        print("Будет выполнено дополнение незначащими нулями")
        zeros_to_add = SIZE - len(str_to_pad)
        zeros = '0' * zeros_to_add
        return zeros + str_to_pad
    return str_to_pad

def conjunction(str1: str, str2: str) -> str:
    result = ""
    for i in range(SIZE):
        result += '1' if str1[i] == '1' and str2[i] == '1' else '0'
    return result

def output_string(str_to_output: str, n: int):
    prompt_text = outPromptTemplate.format(N=n)
    print(prompt_text)
    print(str_to_output)

def output_res(res: str):
    print(f"{outPromptRes}: {res}")

if __name__ == "__main__":   
    temp1 = input_string(1)
    while not check_string(temp1):
        temp1 = input_string(1)
    str1 = add_zeros(temp1)

    temp2 = input_string(2)
    while not check_string(temp2):
        temp2 = input_string(2)
    str2 = add_zeros(temp2)

    res = conjunction(str1, str2)

    output_string(str1, 1)
    output_string(str2, 2)
    output_res(res)