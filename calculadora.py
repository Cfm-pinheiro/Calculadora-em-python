def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def main():
    print("Calculadora Simples")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    choice = int(input("Escolha a operação (1/2/3/4): "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if choice == 1:
        print("Resultado da Soma:", soma(num1, num2))
    elif choice == 2:
        print("Resultado da Subtração:", subtracao(num1, num2))
    elif choice == 3:
        print("Resultado da Multiplicação:", multiplicao(num1, num2))
    elif choice == 4:
        print("Resultado da Divisão:", divisao(num1, num2))
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
