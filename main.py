SIZE = 8

class BitString:
    def __init__(self, input_value=None):
        if input_value is None:
            self.bs = ['0'] * SIZE
        elif isinstance(input_value, str):
            if len(input_value) > SIZE:
                print(f"Длина строки не должна превышать {SIZE} символов!")
                self.bs = ['0'] * SIZE
                return
            for char in input_value:
                if char not in ('0', '1'):
                    print("Строка должна содержать только '0' и '1'.")
                    self.bs = ['0'] * SIZE
                    return
            self.bs = list(input_value.zfill(SIZE))
        elif isinstance(input_value, BitString):
            self.bs = input_value.bs.copy()
        else:
            self.bs = ['0'] * SIZE

    def __del__(self):
        pass
        # Примечание, деструктор реализован, однако Python не требует явного вызова функций при уничтожении объектов для освобождения ресурсов

    def input(self, n: int):
        prompt = f"Введите {n}-ю строку: "
        print(prompt, end="")
        user_input = input()
        temp = BitString(user_input)
        self.bs = temp.bs

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