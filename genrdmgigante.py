from random import randint

def genrdmgigante():
  nr = []
  # ciclo configurado segun el requerimiento del ejercicio,
  # se coloca comentado ya que el proceso consumo mas RAM de la disponible y falla.
  #for x in range(0,10000000):
    #b = [randint(0,5000) for i in range(50000000000)]
    #nr.append(b)
  # en su lugar se configura el mismo proceso con un numero de elementos menor:
  for x in range(0,100):
    b = [randint(0,5000) for i in range(5000)]
    nr.append(b)
  return nr