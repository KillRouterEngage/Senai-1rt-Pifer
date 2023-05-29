salario=float(input("informe o seu salario: "))
if salario > 8250:
   diferença = salario *0.10
   aumento1 = diferença + salario
   print ("seu novo salario",aumento1)
if salario <= 8250:
   diferença2 = salario *0.15
   aumento2 = diferença2 + salario 
   print ("seu novo salario",aumento2)