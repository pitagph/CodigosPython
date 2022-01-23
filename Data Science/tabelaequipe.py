from xml.etree import ElementTree as et
# O comando parse do modulo XML.etree / ElementTree, "parse" FAZ A LEITURA DO ARQUIVO E GUARDA NA VARIAVEL conteudo.... Obs. Banco de dados tem que está na mesma pasta do projeto
conteudo = et.parse("times.xml")

# O comando findall server para retornar uma lista guardada no arquivo xml
lista_equipes = conteudo.findall("equipe")

# Comando de saida Numero de times que existem no banco
print("Numero de Equipes no Campeonato: ", len(lista_equipes))
print("===============================")
# For imprimi todos os dados do arquivo
for item in lista_equipes:
    print("Nome: ", item.find("nome").text)
    print("Posição: ", item.find("posicao").text)
    print("Descrição: ", item.find("descricao").text)
