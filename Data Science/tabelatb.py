import csv

with open('dados.csv', encoding='utf-8') as arq_ref:
    tabela = csv.reader(arq_ref, delimiter=',')

    for l in tabela:
        null01 = l[0]
        null02 = l[1]
        null03 = l[2]
        null04 = l[3]

        print(null01,null02,null03,null04)