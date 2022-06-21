from genrdm import num_random
## importo los numeros aleatorios 
def minigenr():
    list= num_random()
    minimo = list[0]
    for i in range(0, len(list)):
        if list[i] < minimo:
            minimo = list[i]
    return minimo
  
  ## recorro la lista para que arroje el minimo valor 
