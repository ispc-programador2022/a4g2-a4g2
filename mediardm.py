from genrdm import genrdm


def mediardm():
    m=genrdm()
    return sum(m)/len(m)

print(mediardm())
    
#llamo la función genrdm para crear un vector aleatorio y luego devuelvo
#su sumatoria dividido su longitud para calcular la media
#Emmanuel Den Dauw
