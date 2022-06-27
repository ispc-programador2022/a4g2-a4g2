


def medianardm(vector): #La mediana es el valor del medio, es decir con tantos numero mayores como menores en una lista ordenada de numeros.
    
    
    vector.sort()     # Ordeno el vector 
    
    return vector [len(vector) // 2]  #Extraigo el valor de la mitad del vector ordenado.

