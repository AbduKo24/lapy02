def kalkulator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        print("Input tidak valid")
        exit()
    
a = int(input("Masukan angka pertama: "))
b = int(input("Masukan angka kedua: "))
operator = input ("Masukan operator '+', '-', '*', atau '/'") 

hasil = kalkulator(a, b, operator)
print(f"Hasilnya adalah : {hasil}")               