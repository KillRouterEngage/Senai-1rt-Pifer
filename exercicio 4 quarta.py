distancia = float(input("informe a distancia percorrida em km's: "))
if distancia > 200:
    pagamento = distancia *0.45
    print ("o total da viagem será: ",pagamento)
else:
    pagamento2 = distancia *0.50
    print ("o total da viagem será: ",pagamento2)