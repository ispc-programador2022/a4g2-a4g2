from operator import imod


def Vargen50m(listax):
    list= listax
    larg= len(list)
    media= sum(list)/ larg
    desvia= [(x - media) ** 2 for x in list]
    varianza = sum(desvia) / larg
    return varianza