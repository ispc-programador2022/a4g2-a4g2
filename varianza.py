#  función que calcule la varianza del vector obtenido en genrnd.

def Vargen(numalea):
    list= numalea
    larg= len (list)
    media= sum(list)/larg
    desvia= [(x - media) ** 2 for x in list]
    varianza = sum (desvia) / larg
    return varianza

    #Colaboracion Carla Contreras