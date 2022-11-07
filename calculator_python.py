# Calculadora em Python

print("\n =-=-=-=-=-=-=-=-=-=-=-=- Python Calculator -=-=-=-=-=-=-=-=-=-=-=-=")

continuar = 'S'

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

    # O teste identifica se o valor 1 é um número
    try:
        num1 = int(input("\nDigite o primeiro número: "))
    except ValueError:
        print("Isso não é um número.")

        
    print("\nSelecione o número da operação desejada: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Porcentagem")
    print("6 - Potenciação")

    # O teste identifica se a escolha é um número
    try:
        escolha = input("\nDigite sua opção (1/2/3/4/5/6): ")
    except:
        print("Isso não é um número.")

    # O teste identifica se o valor 2 é um número

    num2 = int(input("\nDigite o segundo número: "))


    if escolha == '1':
        print("\n")
        print(num1, "+", num2, "=", add(num1, num2))
        print("\n")

    elif escolha == '2':
        print("\n")
        print(num1, "-", num2, "=", subtract(num1, num2))
        print("\n")

    elif escolha == '3':
        print("\n")
        print(num1, "*", num2, "=", multiply(num1, num2))
        print("\n")

    elif escolha == '4':
        try:
            print("\n")
            print(num1, "/", num2, "=", divide(num1, num2))
            print("\n")
        except ZeroDivisionError:
            print("Não é possível dividir por zero")

    elif escolha == '5':
        print("\n")
        print(num1, "% de ", num2, "=", percentage(num1, num2))

    elif escolha == '6':
        print("\n")
        print(num1, "potência", num2, "=", potentiation(num1, num2))

    else:
        print("\nA opção escolhida não existe!")

    continuar = str(input('Deseja realizar outra operação? (S/N): ').upper())
