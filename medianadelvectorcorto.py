


def medianardm(lista): #La mediana es el valor del medio, es decir con tantos numero mayores como menores en una lista ordenada de numeros.
    
    
    lista.sort()     # Ordeno el vector 
    
    return lista [len(lista) // 2]  #Extraigo el valor de la mitad del vector ordenado.

