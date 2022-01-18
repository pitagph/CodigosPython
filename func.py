def taximetro(distancia, multiplicador = 1):
    largada = 3
    km_rodado = 2
   # return (largada + distancia * km_rodado) * multiplicador
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor
print("Distancia pecorrida 3.5KM")
pagamento = taximetro(3.5)
print("Valor:  R$",pagamento)
#print(pagamento)