class BitString:
    def __init__(self, value=None, size=None):
        """
        Конструктор по умолчанию и с параметрами
        value: может быть строкой или другим объектом BitString
        size: желаемый размер битовой строки
        """
        self.bits = []
        self.size = 0
        
        if value is None:
            # Конструктор по умолчанию
            self.size = size if size is not None else 8
            self.bits = ['0'] * self.size
        elif isinstance(value, str):
            # Конструктор инициализации из строки
            if not self.from_string(value):
                # Если валидация не прошла, создаем по умолчанию
                self.size = size if size is not None else 8
                self.bits = ['0'] * self.size
        elif isinstance(value, BitString):
            # Конструктор копирования
            self.size = value.size
            self.bits = value.bits.copy()  # Глубокое копирование
        
    def __del__(self):
        """Деструктор"""
        print("Объект уничтожен")
    
    def from_string(self, input_string: str) -> bool:
        """Инициализация из строки с валидацией"""
        # Проверка на допустимые символы
        for char in input_string:
            if char not in ('0', '1'):
                print("Ошибка: строка должна содержать только '0' и '1'")
                return False
        
        # Устанавливаем биты
        self.bits = list(input_string)
        self.size = len(input_string)
        return True
    
    def resize(self, new_size: int):
        """Изменение размера битовой строки"""
        if new_size < 0:
            print("Ошибка: размер не может быть отрицательным")
            return
            
        if new_size > self.size:
            # Увеличиваем размер, дополняем нулями
            self.bits.extend(['0'] * (new_size - self.size))
        else:
            # Уменьшаем размер, обрезаем
            self.bits = self.bits[:new_size]
        
        self.size = new_size
    
    def set_bit(self, pos: int, value: str):
        """Установка конкретного бита"""
        if pos < 0 or pos >= self.size:
            print(f"Ошибка: позиция {pos} вне границ [0, {self.size-1}]")
            return
        
        if value not in ('0', '1'):
            print("Ошибка: значение бита должно быть '0' или '1'")
            return
            
        self.bits[pos] = value
    
    def get_bit(self, pos: int) -> str:
        """Получение значения бита"""
        if pos < 0 or pos >= self.size:
            print(f"Ошибка: позиция {pos} вне границ [0, {self.size-1}]")
            return None
        return self.bits[pos]
    
    def get_size(self) -> int:
        """Возвращает текущий размер"""
        return self.size
    
    def conjunction(self, other):
        """Логическое И с другой битовой строкой"""
        if not isinstance(other, BitString):
            print("Ошибка: параметр должен быть BitString")
            return None
            
        min_size = min(self.size, other.size)
        result = BitString(size=min_size)
        
        for i in range(min_size):
            result.bits[i] = '1' if self.bits[i] == '1' and other.bits[i] == '1' else '0'
        
        return result
    
    def input(self, n: int):
        """Ввод битовой строки"""
        prompt = f"Введите {n}-ю строку: "
        print(prompt, end="")
        user_input = input()
        if not self.from_string(user_input):
            # Если ввод некорректен, устанавливаем нулевую строку
            self.bits = ['0'] * self.size
    
    def output(self, n: int):
        """Вывод битовой строки"""
        prompt_text = f"{n}-я строка (с нулями): "
        print(prompt_text)
        print(''.join(self.bits))
    
    def __str__(self) -> str:
        """Строковое представление"""
        return ''.join(self.bits)
    
    def __repr__(self) -> str:
        """Представление для отладки"""
        return f"BitString('{''.join(self.bits)}', size={self.size})"