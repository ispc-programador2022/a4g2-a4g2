def restagenrdm(listax):
    lista=listax #generamos la lista de aleatorios invocando a genrdm
    total=[] #creamos una lista para acumular los resultados de las diferencias de cada combinacion
    for i in range(0,len(lista)): #recorremos la lista restando los elementos conbinados
        for j in range(0,len(lista)):
            if i != j:
              total.append(lista[i] - lista[j])
    rst=total[0] #asignamos a rst el primer valor de la lista
    for i in range(1,len(total)): #recorremos la lista de resultados restandolos entre si
      rst=rst-total[i]
    return rst

#generamos esta funcion ya que el ejercicio 14 y 15 son identicos
#devuelve la diferencia de todas las combinaciones posibles tomados de 2 en 2