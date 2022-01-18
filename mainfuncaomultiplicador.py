def multiplicador(numero):
    a = 20 #variavel Local
    print(f"Dentro da função, a variavel a vale: {a}")
    return a * numero

a = 3 #variavel GLOBAL
b = multiplicador(5)
print(f"Fora de Função, a variavel a vale : {a}")
print(f"Passando um numero pela função multiplicador o resultado será: {b}")

