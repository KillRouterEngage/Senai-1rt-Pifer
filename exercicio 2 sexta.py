from time import sleep 
def contagem_regressiva(num):
    while num > 0:
        num = num - 1
        print(num)
        sleep(1)
contagem = int(input("Declare o valor da contagem regressiva: "))
print (contagem_regressiva)
contagem_regressiva(contagem)