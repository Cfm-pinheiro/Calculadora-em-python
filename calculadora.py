def soma(a, b):
    """
    Função para somar dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Soma dos números
    """
    return a + b

def subtracao(a, b):
    """
    Função para subtrair dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Subtração dos números
    """
    return a - b

def mutiplicacao(a, b):
    """
    Função para multiplicar dois números.
    :param a: Primeiro número
    :param b: Segundo número
    :return: Multiplicação dos números
    """
    return a * b

def divisao(a, b):
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

try:
    escolha = int(input("Escolha a operação (1/2/3/4): "))

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == 1:
        print("Resultado da Soma:", soma(num1, num2))
    elif escolha == 2:
        print("Resultado da Subtração:", subtracao(num1, num2))
    elif escolha == 3:
        print("Resultado da Multiplicação:", mutiplicacao(num1, num2))
    elif escolha == 4:
        print("Resultado da Divisão:", divisao(num1, num2))
    else:
        print("Opção inválida!")
except ValueError:
    print('Entrada inválida. Certifique-se de digitar números válidos.')

if __name__ == "__main__":
    main()
