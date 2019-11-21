def inverte_matriz(matriz):
    a = matriz[0][0]
    b = matriz[0][1]
    c = matriz[1][0]
    d = matriz[1][1]

    if(a*d ==b*c):
        return none

    else:
        detA = a*d-b*c
        matriz_inversa = ((d/detA,-b/detA),(-c/detA , a/detA))
        return matriz_inversa
def main():
    a = float(input('Entre com o ponto (0,0)'))
    b = float(input('Entre com o ponto (0,1)'))
    c = float(input('Entre com o ponto (1,0)'))
    d = float(input('Entre com o ponto (1,1)'))
    matriz_a = ([a,b],[c,d])
    inversa_a = inverte_matriz(matriz_a)
    print(str(matriz_a[0])+'\t'+str(inversa_a[0]))
    print(str(matriz_a[1])+'\t'+str(inversa_a[1]))

main()
        

