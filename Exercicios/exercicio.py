def learq(arq):
    arq.seek(0,0)
    lista = arq.readlines()
    turma =[]
    for line in lista:
        line = line[:-1]
        line_split = line.split(':')

        aluno = {'nome':line_split[0],
        'idade':line_split[1],
        'Mãe':line_split[2],
        'Irmãos':line_split[3:]
        } 
        turma+= [aluno]
        return turma

    

def dic_texto():
    
    arq = open('registro_alunos.txt','r+')
    nome = input('Entre com o nome do aluno''\n')
    idade = input('Entre com a idade''\n')
    nome_mãe = input('Entre com o nome da mãe''\n')
    irmão1= input('Entre com o nome do primeiro irmão(a)''\n')
    irmão2=input('Entre com o nome do segundo irmão(a)''\n')
    irmãos = irmão1 + irmão2
    listirmãos = list(irmãos)
    texto = nome + ':' + idade +':' +  nome_mãe +':' +  irmãos 
    arq.writelines(texto)


    turma = learq(arq)
    print(arq.readlines())
    print(turma)
    return

dic_texto()            
        
    
