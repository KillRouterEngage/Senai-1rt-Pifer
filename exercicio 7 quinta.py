cont = 0

while True:
    resp = int(input("insira um número: "))
    if cont < 0:
        break
    if cont %2 == 0:
        print("O numero é par", resp)
        cont = resp +2
    else:
        print("O numero é impar",resp)
        cont= resp + 1
    