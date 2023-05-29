num1 = int(input("insira um valor: "))
num2 = int(input("insira um valor: "))
num3 = int(input("insira um valor: "))

def maior(num1, num2, num3):
    menor = min(num1,num2,num3)
    maisgrande= max(num1,num2,num3)
    return (menor,maisgrande)

print ("o menor e o maior número são: ") 
print (maior(num1,num2,num3))