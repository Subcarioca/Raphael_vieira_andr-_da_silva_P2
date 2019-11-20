def dic_data(data):
    lines_split = lines.split('/')
    dic_data = {'Ano': lines_split[:0],
    'Mês':lines_split[1],
    'Dia':lines_split[2]}
    return(dic_data)
dic_data(data)






def lista_string(string):
    lista_string = string.split(':')
    return lista_string
lista_string(string)

def lerarq(arq):
    arq.seek(0,0)
    read.arq = read.lines(arq)
    lista_informação = []
    for line in read.arq:
        lista_informação.append(line)
        arq.close
        return
lerarq(arq)


def main():
    arq = open('cadastro.txt', 'r+')
    lista = []
    lista_cadastro = lista.arq()
    for cadastro in lista_cadastro:
        CPF = lista_informação[0]
        Nome = lista_informação[1]
        data_nascimento = lista_informação[2]
        data_cadastro = dic_data_info[3]
        ativo = cadastro_info[4]

        
