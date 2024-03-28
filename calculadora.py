def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

# Exemplo de uso
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Soma:", add(num1, num2))
print("Subtração:", subtract(num1, num2))
print("Multiplicação:", multiply(num1, num2))
print("Divisão:", divide(num1, num2))

