def taximetro(dist):
    def calculaML():
        if dist < 5:
            return 1.2
        else:
            return 1
        multi = calculaML()
        largada = 3
        km_rodado = 2
        return (largada + dist * km_rodado) * multi

    distancia = eval(input("Entre com a distancia a ser percorrida em km:"))
    pagamento = taximetro(distancia)
    print(f'O valor a pagar é R$ {pagamento}')
