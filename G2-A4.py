## Esta aplicación debe llamar a funciones, cada una en su archivo .py 
from cartel import cartel
print(cartel())
from fing2i import ing2i
from fing2s import ing2s
from suma import suma
from resta import rest
from producto import producto
from cociente import cociente
from modulo import modulo
from potencia import potencia
from raiz import raiz
## asignamos los valores para las operaciones
enteros= ing2i()
str= ing2s()


print("Operación Suma de Enteros: ", enteros[0], "+", enteros[1], "=", suma(enteros[0],enteros[1]))
print("Operación Resta de Enteros: ", enteros[0], "-", enteros[1], "=", rest(enteros[0],enteros[1]))
print("Operación Producto de Enteros: ", enteros[0], "*", enteros[1], "=", producto(enteros[0],enteros[1]))
print("Operación Cociente de Enteros: ", enteros[0], "/", enteros[1], "=", cociente(enteros[0],enteros[1]))
print("Operación Módulo de Enteros: ", enteros[0], "%", enteros[1], "=", modulo(enteros[0],enteros[1]))
print("Operación Potencia de Enteros: ", enteros[0], "**", enteros[1], "=", potencia(enteros[0],enteros[1]))
print("Operación Radicación de Enteros: ", enteros[1], "√", enteros[0], "=", raiz(enteros[0],enteros[1]))

