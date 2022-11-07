# Calculadora em Python

print("\n =-=-=-=-=-=-=-=-=-=-=-=- Python Calculator -=-=-=-=-=-=-=-=-=-=-=-=")

continuar = 'S'

# Estrutura de Repetição que pergunta se o Cliente deseja fazer um novo calculo
while continuar == 'S':

    # Funçao para Adição
    def add(x, y):
        return x + y

    # Função para Subtração
    def subtract(x, y):
        return x - y

    # Função para Multiplicação
    def multiply(x, y):
        return x * y

    # Função para Divisão
    def divide(x, y):
        return x / y

    # Função para Porcentagem
    def percentage(x, y):
        return (x * y) / 100

    # Função para Potenciação
    def potentiation(x, y):
        return x ** y

    # O teste identifica se o valor foi realmente digitado e se ele é um número:
    
    def configInt(message):
        ok = False
        valor = 0
        while True:
            n = str(input(message))
            if n.isnumeric():
                valor = int(n)
                ok = True
            else:
                print('ERRO! Digite um número inteiro válido! \n')
            if ok:
                break
        return valor

    num1 = configInt('\n Digite o primeiro valor: ')

# O teste identifica se a escolha é um número
    def configInt1a6(message):
        ok = False
        valor = 0
        while True:
            n = str(input(message))
            if n.isnumeric():
                valor = int(n)
                ok = True
            elif n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
                valor = int(n)
                ok = True
            else:
                print('\n ERRO! Digite uma opção válida!')
            if ok:
                break
        return str(valor)
        
    print("\n Selecione o número da operação desejada: \n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Porcentagem\n 6 - Potenciação\n")

    escolha = configInt1a6("\n Digite sua opção (1/2/3/4/5/6): ")

    # Variável para o valor 2
    num2 = configInt("\n Digite o segundo número: ")
 
    
    # Condição para Adição
    if escolha == '1':
        print(f"\n {num1} + {num2} = {add(num1, num2)} \n")

    # Condição para Subtração
    elif escolha == '2':
        print(f"\n {num1} - {num2} = {subtract(num1, num2)} \n")

    # Condição para Multiplicação
    elif escolha == '3':
        print(f"\n {num1}  x {num2} = {multiply(num1, num2)} \n")

    # Condição para Divisão
    elif escolha == '4':
        try:
            print(f"\n {num1} / {num2} = {divide(num1, num2)} \n")
        except ZeroDivisionError:
            print("\n Não é possível dividir por zero \n")
        finally:
            print("\n O segundo valor da divisão é zero, por favor, tente novamente. \n")

    # Condição para Porcentagem
    elif escolha == '5':
        print(f"\n {num1}% de {num2} = {percentage(num1, num2)} \n")

    # Condição para Potenciação
    elif escolha == '6':
        print(f"\n {num1} expoente {num2} = {potentiation(num1, num2)} \n")

    continuar = str(input('Deseja realizar outra operação? (S/N): ').upper())
