SIZE = 8

class BitString:
    def __init__(self, input_string=""):
        self.bs = ['0'] * SIZE
        if input_string:
            self.from_string(input_string)

    def from_string(self, input_string: str):
        if len(input_string) > SIZE:
            print(f"Длина строки не должна превышать {SIZE} символов!")
            return
        for char in input_string:
            if char not in ('0', '1'):
                print("Строка должна содержать только '0' и '1'.")
                return
        self.bs = list(input_string.ljust(SIZE, '0')[:SIZE])

    def input(self, n: int):
        prompt = f"Введите {n}-ю строку: "
        print(prompt, end="")
        user_input = input()
        self.from_string(user_input)

    def output(self, n: int):
        prompt_text = f"{n}-я строка (с нулями): "
        print(prompt_text)
        print(''.join(self.bs))

    def conjunction(self, other):
        result = BitString()
        for i in range(SIZE):
            result.bs[i] = '1' if self.bs[i] == '1' and other.bs[i] == '1' else '0'
        return result

def main():
    a = BitString()
    b = BitString()
    a.input(1)
    b.input(2)
    c = a.conjunction(b)
    a.output(1)
    b.output(2)
    print("Результат:")
    c.output(3)

if __name__ == "__main__":
    main()
