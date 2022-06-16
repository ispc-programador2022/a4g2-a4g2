# 14- función que devuelva el producto de las combinaciones posibles de los 
# números generados por la función genrnd tomados de a dos.
def progen():
    lista=genrdm()
    total=0
    for i in range(0,len(lista)-1):
        for j in range(i+1,len(lista)):
            total*= lista[i] * lista[j]
    return total