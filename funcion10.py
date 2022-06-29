import suma
import producto

def  ejercicio_10(a,b,c):
    sum = 0
    multi = 0

    sum = suma.suma(a,b) #llamo  a la funcion de Suma del modulo Suma y cargo en la variable sum la suma de a y b.

    multi = producto.producto( sum, c) #llamo a la funcion producto del modulo producto y multiplico el valor de la suma por la variable c

    return (multi) 

