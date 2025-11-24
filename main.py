from bitstring import BitString

SIZE = 8

def main():
    a = BitString()
    b = BitString()
    
    a >> 1
    b >> 2
    
    c = a & b
    
    a << 1
    b << 2
    print("Результат конъюнкции:")
    c << 3
    
if __name__ == "__main__":
    main()