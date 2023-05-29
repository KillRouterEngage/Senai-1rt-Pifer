def somar(num1,num2):
    return num1 + num2

def multiplicar(num1,num2):
    return num1 * num2

def menor(num1,num2):
    return min(num1,num2)

def maior(num1,num2):
    return max(num1,num2)

print("Escolha uma das opções abaixo:")
print("a. Adição")
print("b. Multiplicação")
print("c. Menor número")
print("d. Maior número")

opcao = input("Opção: ")
num1 = float(input("Insira o valor 1: "))
num2 = float(input("Insira o valor 2: "))

if opcao == "a":
    resultado = somar(num1,num2)
    print("A soma é", resultado)
elif opcao == "b":
    resultado = multiplicar(num1,num2)
    print("O produto é", resultado)
elif opcao == "c":
    resultado = menor(num1,num2)
    print("O menor número é", resultado)
elif opcao == "d":
    resultado = maior(num1,num2)
    print("O maior número é", resultado)

