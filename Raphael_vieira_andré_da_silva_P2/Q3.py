def isCollisionDetected(coordA,coordB):
    if(coordA('bottomleft')[0]<coordB['bottomleft'[0]]):

        retanguloesquerdo = dict(coordA)
        retangulodireito = dict(coordB)

    else:
        retanguloesquerdo = coordB
        retangulodireito = coordA
    x = retangulodireito['bottomlef']
def vertice():
    BLx = float(input('Entre com BLx'))
    BLy = float(input('Entre com BLy'))
    TRx = float(input('Entre com TRx'))
    TRy = float(input('Entre com TRy'))
    retangulo = {'bottomLeft':[BLx,BLy],'TopRight:[TRx,TRy]'}
    return retangulo

def main():
    retanguloA = vertice()
    retanguloB = vertice()

        if isCollisionDetected(retanguloaA,retanguloB)==True:
            print ('Colisão detectada')

        else:
            print('Colisão não detectada')
