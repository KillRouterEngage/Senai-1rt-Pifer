numero1 = float(input("insira um valor: "))
numero2 = float(input("insira outro valor: "))
operador = (input("insira um operador: "))

if operador == "/":
    resultado = numero1 / numero2 
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "-":
    resultado = numero1 - numero2
else:
    resultado = numero1 + numero2

print (resultado)
