def Nob(a,b):


    valor1=a//10
    valor2=a%10
    valor3=b//10
    valor4=b%10
    soma1=valor1 + valor2
    soma2=valor3 + valor4
    c = soma1+soma2
    return(c)
a = int(input('Entre com um numero'))
b = int(input('Entre com um numero'))
print(Nob(a,b))

