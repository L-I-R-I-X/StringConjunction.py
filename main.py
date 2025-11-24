from bitstring import ExtendedBitString

SIZE = 8

def main():
    a = ExtendedBitString()
    b = ExtendedBitString()
    
    a >> 1
    b >> 2
    
    c = a & b
    
    a << 1
    b << 2
    print("Результат конъюнкции:")
    c << 3
    
if __name__ == "__main__":
    main()