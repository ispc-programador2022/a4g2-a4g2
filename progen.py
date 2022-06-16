# 14- función que devuelva el producto de las combinaciones posibles de los 
# números generados por la función genrnd tomados de a dos.

## Llamo a la funcion genrnd de 50 num aleatorios
def progen():
    lista=genrdm()
    total=0
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            total*= lista[i] * lista[j]
    return total
## Recorro la lista asignando i y j para sacar la suma de las combinanciones posibles de los numeros aleatorios tomados de a dos
##Ejercicio realizado con colaboración de Chacón Claudio