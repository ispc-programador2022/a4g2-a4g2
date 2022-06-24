from genrdm import genrdm #importo el modulo

def maxgenrdm():# defino la funcion
    numeros=genrdm()#llamo a genrdm que devuelve lista de 50 valores aleatorios
    return max(numeros)#uso la funcion max para identificar el valor maximo de la lista y lo devuelvo al main