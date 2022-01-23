import csv

with open('aluno.csv', encoding='utf-8') as arq_ref:
        tabela = csv.reader(arq_ref, delimiter=',')
        print("Matricula\t\tNome do Aluno\t\tCurso\t\t\tNota")
        print("====================================================================")
        for l in tabela:
            Matricula = l[0]
            Nome = l[1]
            Curso = l[2]
            Nota = l[3]
            print("%s------------%s-----%s-----%s\t\t\t" % (Matricula, Nome, Curso, Nota))