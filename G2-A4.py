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
## Modificar nombre de Ejercicio 10 como py
from funcion11 import funcion11
from genrdm import genrdm ## modificar funcion sacar print
from sumagenrd import sumgenr
from progen import progen## modificar  funcion asignarle una lista x ejemplo def progenr(numalea): lista= numalea
from maxgenrdm import maxgenrdm ##modificar funcion sacar el import genrdm
from minigen import min_genrnd
from mediardm import mediardm## quitar print modificar  funcion asignarle una lista x ejemplo def media(numalea): lista= numalea
## Modificar Nombre Mediana del vector como py, quitar print e import del genrdm, asignarle una lista x
from varianza import Vargen
##FUNCIONES PENDIENTES BLOQUE 4
## asignamos los valores para las operaciones
enteros= ing2i()
str= ing2s()
numrand=genrdm()

print("Operación Suma de Enteros: ", enteros[0], "+", enteros[1], "=", suma(enteros[0],enteros[1])) ##1- función suma
print("Operación Resta de Enteros: ", enteros[0], "-", enteros[1], "=", resta(enteros[0],enteros[1])) ##2- función resta
print("Operación Producto de Enteros: ", enteros[0], "*", enteros[1], "=", producto(enteros[0],enteros[1])) ##2- función resta
print("Operación Cociente de Enteros: ", enteros[0], "/", enteros[1], "=", cociente(enteros[0],enteros[1])) ## 4- función cociente
print("Operación Módulo de Enteros: ", enteros[0], "%", enteros[1], "=", modulo(enteros[0],enteros[1])) ##5- función módulo
print("Operación Potencia de Enteros: ", enteros[0], "**", enteros[1], "=", potencia(enteros[0],enteros[1])) ##6- función potencia
print("Operación Radicación de Enteros: ", enteros[1], "√", enteros[0], "=", raiz(enteros[0],enteros[1])) ##7- función radicación
print("Ingrese Tercer parametro para operar: ")
enteros.append(int(input()))
print("Operación Producto de los 2 Enteros mas el Tercer Parametro es= ", funcion9(enteros[0],enteros[1],enteros[2]))
print("Operación Resta de los 2 Enteros por el Tercer Parametro es= ", funcion11(enteros[0],enteros[1],enteros[2]))

print("Numeros aleatorios: ", numrand)
print("Suma de las Combinaciones posibles Genrnd tomados de a dos: ", sumgenr(numrand))
#print("Producto de las Combinaciones posibles Genrnd tomados de a dos: ", progen(numrand))

## iniciar cuenta tiempo ejecucion ejercicio 29
#print("Media de Los Numeros aleatorios: ", mediardm(numrand))
#print("Mediana de Los Numeros aleatorios: ", median(nr))
#print("Rango de Los Numeros aleatorios: ", rangogen(numrand))
print("La Varianza de Los Numeros aleatorios: ", Vargen(numrand))
print("El minimo del vector de Los Numeros aleatorios: ", min_genrnd(numrand))
#print("El maximo del vector de Los Numeros aleatorios: ", maxgenrdm(numrand))
## Finalizar cuenta tiempo ejecucion ejercicio 29

## iniciar cuenta tiempo ejecucion ejercicio 30

#print("La media de los 50M Numeros Aleatorios : ", media5m(alea500))
#print("La mediana de los 50M Numeros Aleatorios : ", median50m(alea500))
#print("Rango de Los 50M Numeros Aleatorios : ", rango50m(alea500))
#print("La Varianza de  Los 50M Numeros Aleatorios : ", Vargen50m(alea500))
#print("El minimo del vector de Los 50M Numeros aleatorios: ", min_50m(alea500))
#print("El maximo del vector de Los 50M Numeros aleatorios: ", maxgenr50m(alea500))
## Finalizar cuenta tiempo ejecucion ejercicio 30
