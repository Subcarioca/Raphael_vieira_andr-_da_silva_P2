def learq(arq):
    cont = 0
    arq.seek(0,0)
    lista = arq.realines()
    for line in lista:
        line = line[:-1]
    line_split=lines.split(':')
    aluno = {'Nome': line_split[:0],
    'Idade': line_split[1],
    'Nome Mãe':line_split[2],
    'Irmãos':line_split[3]}
    registro = []
    registro += [aluno]
    for cont in registro(3,len(registro)):
        
    print(registro)
    return
def main():
    arq = open('registro_alunos2.txt','w')
    nome = input('Entre com o nome' '\n')
    idade = input('Entre com a idade''\n')
    nome_mãe = input('Entre com o nome da mãe''\n')
    nome_irmão1 = input('Entre com o nome do irmão''\n')
    nome_irmão2 = input('Entre com o nome do segundo irmão''\n')
    idade_irmão1 = input('Entre com a idade do primeiro irmão''\n')
    idade_irmão2 = input('Entre com a idade do segundo irmão''\n')
    irmãos = nome_irmão1 + ':' + idade_irmão1 + ':' + nome_irmão2 + ':'+ idade_irmão2
    lista_irmãos = []
    lista_irmãos.append(irmãos)
    texto = nome + ':' + idade + ':' +  nome_mãe + ':'
    texto.append(lista_irmãos)
    registro_alunos = []
    registro_alunos.writelines(texto)
    return arq

main()