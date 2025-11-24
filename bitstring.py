class BitStringError(Exception):
    pass

class BitString:
    def __init__(self, value=None, size=None):
        self.bits = []
        self.size = 0
        
        if value is None:
            self.size = size if size is not None else 8
            self.bits = ['0'] * self.size
        elif isinstance(value, str):
            try:
                if not self.from_string(value):
                    self.size = size if size is not None else 8
                    self.bits = ['0'] * self.size
            except BitStringError:
                self.size = size if size is not None else 8
                self.bits = ['0'] * self.size
        elif isinstance(value, BitString):
            self.size = value.size
            self.bits = value.bits.copy()
        
    def __del__(self):
        print("Объект уничтожен")
    
    def from_string(self, input_string: str) -> bool:
        for char in input_string:
            if char not in ('0', '1'):
                raise BitStringError("Ошибка: строка должна содержать только '0' и '1'")
        
        self.bits = list(input_string)
        self.size = len(input_string)
        return True
    
    def resize(self, new_size: int):
        if new_size < 0:
            raise BitStringError("Ошибка: размер не может быть отрицательным")
            
        if new_size > self.size:
            self.bits.extend(['0'] * (new_size - self.size))
        else:
            self.bits = self.bits[:new_size]
        
        self.size = new_size
    
    # Перегрузка оператора [] для получения бита
    def __getitem__(self, pos: int) -> str:
        if pos < 0 or pos >= self.size:
            raise BitStringError(f"Ошибка: позиция {pos} вне границ [0, {self.size-1}]")
        return self.bits[pos]
    
    # Перегрузка оператора [] для установки бита
    def __setitem__(self, pos: int, value: str):
        if pos < 0 or pos >= self.size:
            raise BitStringError(f"Ошибка: позиция {pos} вне границ [0, {self.size-1}]")
        
        if value not in ('0', '1'):
            raise BitStringError("Ошибка: значение бита должно быть '0' или '1'")
            
        self.bits[pos] = value
    
    def set_bit(self, pos: int, value: str):
        self[pos] = value
    
    def get_bit(self, pos: int) -> str:
        return self[pos]
    
    def get_size(self) -> int:
        return self.size
    
    # Перегрузка оператора & для конъюнкции
    def __and__(self, other):
        if not isinstance(other, BitString):
            raise BitStringError("Ошибка: параметр должен быть BitString")
            
        min_size = min(self.size, other.size)
        result = BitString(size=min_size)
        
        for i in range(min_size):
            result.bits[i] = '1' if self.bits[i] == '1' and other.bits[i] == '1' else '0'
        
        return result
    
    def conjunction(self, other):
        return self & other
    
    # Перегрузка оператора >> для ввода
    def __rshift__(self, n: int):
        prompt = f"Введите {n}-ю строку: "
        print(prompt, end="")
        user_input = input()
        try:
            if not self.from_string(user_input):
                self.bits = ['0'] * self.size
        except BitStringError as e:
            print(str(e))
            self.bits = ['0'] * self.size
        return self
    
    # Перегрузка оператора << для вывода
    def __lshift__(self, n: int):
        prompt_text = f"{n}-я строка (с нулями): "
        print(prompt_text)
        print(''.join(self.bits))
        return self
    
    def input(self, n: int):
        self >> n
    
    def output(self, n: int):
        self << n
    
    def __str__(self) -> str:
        return ''.join(self.bits)
    
    def __repr__(self) -> str:
        return f"BitString('{''.join(self.bits)}', size={self.size})"