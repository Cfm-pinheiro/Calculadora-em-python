def add(a, b):
    """
    Função para somar dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma dos números
    """
    return a + b

def subtract(a, b):
    """
    Função para subtrair dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Subtração dos números
    """
    return a - b

def multiply(a, b):
    """
    Função para multiplicar dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Multiplicação dos números
    """
    return a * b

def divide(a, b):
    """
    Função para dividir dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Resultado da divisão ou mensagem de erro se b for zero
    """
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
        print("Resultado da Soma:", add(num1, num2))
    elif choice == 2:
        print("Resultado da Subtração:", subtract(num1, num2))
    elif choice == 3:
        print("Resultado da Multiplicação:", multiply(num1, num2))
    elif choice == 4:
        print("Resultado da Divisão:", divide(num1, num2))
    else:
        print("Opção inválida!")

if __name__ == "__main__":
    main()
