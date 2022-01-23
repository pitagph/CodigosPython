def Aluno(Matricula,Nome,Curso,Nota):
    def mk_tabela():
        print("Matricula\t\tNome do Aluno\t\tCurso\t\tNota")
        print("====================================================================")
        print("%s-----%s-----%s-----%f\t\t\t" % (Matricula,Nome,Curso,Nota))
    return mk_tabela()

Aluno(12345,"Phillipe Silva","Sistemas de Informação", 9.0)
Aluno(123467,"Edu","Analise de Sistemas", 8.0)
