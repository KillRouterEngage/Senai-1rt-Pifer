count = 0

while True:
    numero = int(input("Insira um numero: "))
    if count < 0:
        break
    if numero %2 == 0:
        print("O numero é par", numero)
        count = numero + 2
    else:
        print("O numero é impar",numero)
        count = numero + 1