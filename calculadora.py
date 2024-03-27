operacao_de_calcular = input('Selecioone a operação (soma, subtracao, mutoplicacao, divisao): ')
numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))


if operacao_de_calcular == 'soma':
    resultado = numero_1 + numero_2
elif operacao_de_calcular == 'subtracao':
    resultado = numero_1 - numero_2
elif operacao_de_calcular == 'multiplicacao':
    resultado = numero_1 * numero_2
elif operacao_de_calcular == 'divisao':
    if numero_2 != 0:
         resultado = numero_1 / numero_2
    else:
        print('Erro Divisão por zero não é permitido.')

else:
    print('Erro: Operaçao invalida.')
    resultado = None

if resultado is not None:
    print(f'o resultado é: {resultado}')
