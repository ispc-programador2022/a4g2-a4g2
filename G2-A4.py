## Esta aplicación debe llamar a funciones, cada una en su archivo .py 
from cartel import cartel
print(cartel())
from fing2i import ing2i
from fing2s import ing2s
from suma import suma
from resta import resta
from producto import producto
from cociente import cociente
from modulo import modulo
from potencia import potencia
from raiz import raiz
from funcion9 import funcion9
from Ejercicio 10 import Ejercicio 10 #Quitar espacios del nombre del archivo py
from funcion11 import funcion11
from genrdm import genrdm 
from sumagenrd import sumgenr
from progen import progen ## modificar  funcion asignarle una lista x ejemplo def progenr(numalea): lista= numalea
from maxgenrdm import maxgenrdm ## modificar funcion sacar el import genrdm, asignar (listax) numeros=listax
from minigen import min_genrnd
from medianadelvector import mediardm
from Mediana del vector import medianadelvector #Quitar espacios del nombre del archivo py

## asignamos los valores para las operaciones#
enteros= ing2i()
str= ing2s()
numrand=genrdm()
#NR50M= Funcion q genere los 50 ml random()
print("Operación Suma de Enteros: ", enteros[0], "+", enteros[1], "=", suma(enteros[0],enteros[1])) ##1- función suma
print("Operación Resta de Enteros: ", enteros[0], "-", enteros[1], "=", resta(enteros[0],enteros[1])) ##2- función resta
print("Operación Producto de Enteros: ", enteros[0], "*", enteros[1], "=", producto(enteros[0],enteros[1])) ##2- función resta
print("Operación Cociente de Enteros: ", enteros[0], "/", enteros[1], "=", cociente(enteros[0],enteros[1])) ## 4- función cociente
print("Operación Módulo de Enteros: ", enteros[0], "%", enteros[1], "=", modulo(enteros[0],enteros[1])) ##5- función módulo
print("Operación Potencia de Enteros: ", enteros[0], "**", enteros[1], "=", potencia(enteros[0],enteros[1])) ##6- función potencia
print("Operación Radicación de Enteros: ", enteros[1], "√", enteros[0], "=", raiz(enteros[0],enteros[1])) ##7- función radicación
print("Ingrese Tercer parametro para operar: ")
enteros.append(int(input()))## Agregamos Tercer Parametro
print("Operación Producto de los 2 Enteros mas el Tercer Parametro es= ", funcion9(enteros[0],enteros[1],enteros[2]))##9- función p1, retorna el producto

print("Operación Resta de los 2 Enteros por el Tercer Parametro es= ", funcion11(enteros[0],enteros[1],enteros[2]))##10- función p1, retorna la suma

print("Numeros aleatorios: ", numrand)##12- función genrnd
print("Suma de las Combinaciones posibles Genrnd tomados de a dos: ", sumgenr(numrand))##13- función que devuelva la suma 
#print("Producto de las Combinaciones posibles Genrnd tomados de a dos: ", progen(numrand))##14- función que devuelva el producto

## iniciar cuenta tiempo ejecucion ejercicio 29
print("Media de Los 50 Numeros Aleatorios: ", mediardm(numrand))##16- función que calcule la media    
print("Mediana de Los 50 Numeros Aleatorios: ", medianadelvector(numrand))
#print("Rango de Los 50 Numeros Aleatorios: ", rangogen(numrand))
print("La Varianza de Los 50 Numeros Aleatorios: ", Vargen(numrand)) ##19- función que calcule la varianza
print("El minimo del vector de Los 50 Numeros Aleatorios: ", min_genrnd(numrand))##20- función que calcule devuelva el mínimo
#print("El maximo del vector de Los 50 Numeros Aleatorios: ", maxgenrdm(numrand))
## Finalizar cuenta tiempo ejecucion ejercicio 29

## iniciar cuenta tiempo ejecucion ejercicio 30

#print("La media de los 50M Numeros Aleatorios : ", media5m(NR50M))
#print("La mediana de los 50M Numeros Aleatorios : ", median50m(NR50M))
#print("Rango de Los 50M Numeros Aleatorios : ", rango50m(NR50M))
#print("La Varianza de  Los 50M Numeros Aleatorios : ", Vargen50m(NR50M))
#print("El minimo del vector de Los 50M Numeros aleatorios: ", min_50m(NR50M))
#print("El maximo del vector de Los 50M Numeros aleatorios: ", maxgenr50m(NR50M))
## Finalizar cuenta tiempo ejecucion ejercicio 30
#print("Tiempo de ejecucion Funciones 16 a 21: ", fin - inicio) #Ejercicio 29
#print("Tiempo de ejecucion Funciones 22 a 28: ", fin1 - inicio1) #Ejericio 30

print("Python Developer's: \n", "*Chacon Claudio Gabriel\n" ,"*Contreras Carla Daniela\n", "*Contreras Montañana David Ismael\n", "*Cordoba Marcelo Gustavo\n" ,"*Cuestas Natalia Noemi\n", "*Den Dauw Emmanuel\n" )
