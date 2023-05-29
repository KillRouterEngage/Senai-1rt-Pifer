nota = int(input("insira a sua nota: "))
if nota <= 50:
    print ("parabens! você ganhou o certificado de participação!")
elif nota <= 60:
    print ("parabens! você ganhou o certificado de menção honrosa!")
elif nota <= 70:
    print ("parabens! você ganhou a medalha de bronze!")
elif nota <= 90:
    print ("parabens! você ganhou a medalha de prata!")
else:
    print ("parabens! você ganhou a medalha de ouro! ")
