from xml.etree import ElementTree as et
# O comando parse do modulo XML.etree "parse" FAZ A LEITURA DO ARQUIVO E GUARDA NA VARIAVEL conteudo
conteudo = et.parse("times.xml")

# O comando findall server para retornar uma lista guardada no arquivo xml
lista_equipes = conteudo.findall("equipe")

# Comando de saida
print("Equipes: ", len(lista_equipes))

# For imprimi todos os dados do arquivo
for item in lista_equipes:
    print("Nome: ", item.find("nome").text)
    print("Posição: ", item.find("posicao").text)
    print("Descrição: ", item.find("descricao").text)