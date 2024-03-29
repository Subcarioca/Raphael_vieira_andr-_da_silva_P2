def isCollisionDetected(rec1, rec2):
    rec1_xi = rec1["bottomLeft"][0]
    rec1_xf = rec1["topRight"][0]
    rec1_yi = rec1["bottomLeft"][1]
    rec1_yf = rec1["topRight"][1]

    rec2_xi = rec2["bottomLeft"][0]
    rec2_xf = rec2["topRight"][0]
    rec2_yi = rec2["bottomLeft"][1]
    rec2_yf = rec2["topRight"][1]

    if (rec1_xi < rec2_xf and rec1_xf > rec2_xi and rec1_yi < rec2_yf and rec1_yf > rec2_yi):          # a chave da questão está na satisfação dessas condições,pois as coordenadas dos retangulos não podem estar dentro do intervalo de uma das outras nos mesmos eixos.
        return True
    return False

def main():
    rectangle = {"bottomLeft":"",
             "topRight":""}

    BLx = float(input('Entre com o BLx para o primeiro retangulo''\n'))
    BLy = float(input('Entre com o BLy para o primeiro retangulo''\n'))
    TRx = float(input('Entre com o TRx para  o primeiro retangulo''\n'))
    TRy = float(input('Entre com o TRy para o primeiro retamgulo''\n'))

    BL1 = (BLx, BLy)
    TR1 = (TRx, TRy)
    
    rec1 = rectangle.copy()
    rec1["bottomLeft"] = BL1
    rec1["topRight"] = TR1
    
    BLx = float(input('Entre com o BLx para o segundo retangulo'))
    BLy = float(input('Entre com o BLy para o segundo retangulo'))
    TRx = float(input('Entre com o TRx para o segundo retangulo'))
    TRy = float(input('Entre com o TRy para o segundo retangulo '))

    BL2 = (BLx, BLy)
    TR2 = (TRx, TRy)

    rec2 = rectangle.copy()
    rec2["bottomLeft"] = BL2
    rec2["topRight"] = TR2

    colidiu = isCollisionDetected(rec1, rec2)

    if colidiu == True:
        print("Colisao detectada")

    else:
        print("Colisao nao detectada")

main()
