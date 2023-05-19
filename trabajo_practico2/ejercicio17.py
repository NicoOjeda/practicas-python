# 17. Que muestre todos los números primos entre 0 y 100 e imprima cuántos números primos hay.
contador = 0

def numeros_primos():
    contador2= 0
    for i in range(1,101,1):
        contador = 0
        for c in range(1,i+1,1):
            if(i%c ==0):
                contador += 1
                
        if(contador==2):
            print(i)
            contador2 += 1
        else:
            print(i)
    print(f'Entre 0 y 100 hay {contador2} numeros primos')
        
numeros_primos()
