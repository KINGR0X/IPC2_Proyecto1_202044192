from nodo_patron import nodo_patron

class lista_patrones:
  
  def __init__(self):
    self.primero = None
    self.contador_patrones=0

  def insertar_dato(self,patron):
    if self.primero is None:
      self.primero = nodo_patron(patron=patron)
      self.contador_patrones+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_patron(patron=patron)
    self.contador_patrones+=1

  def recorrer_e_imprimir_lista(self):
    print("=== Matriz de patrones ===")
    actual = self.primero
    while actual != None:
      print("Tiempo: ",actual.patron.tiempo,"Cadena-Patron: ",actual.patron.cadena_patron[:-1])
      actual = actual.siguiente
    print(" ")

  # Sirve para eliminar un nivel entero ej: eliminar todos los tiempos 1
  def eliminar(self,tiempo):
    actual = self.primero
    anterior = None
    while actual and actual.patron.tiempo!= tiempo:
      anterior=actual
      actual = actual.siguiente
    # si anterior es None quiere decir que el nodo a eliminar es el primero, entonces ahora el primer nodo es el siguiente del actual
    if anterior is None:
      self.primero = actual.siguiente
      actual.siguiente = None
    elif actual:
      # como queremos eliminar actual, entonces el nodo anterior ahora paunta al siguiente de actual y actual apunta a None, peridendose asi el nodo actual
      anterior.siguiente = actual.siguiente
      actual.siguiente = None

  
  def encontrar_coincidencias(self):
    resultado = ""  # Inicializa un string vacío para almacenar el resultado final  
    # Bucle principal que se ejecuta mientras haya nodos en la lista
    while self.primero:
      actual = self.primero  # Comienza desde el primer nodo en la lista
      temp_string = ""  # String temporal para almacenar tiempo coincidentes
      temp_tiempos= ""  # Lista temporal para almacenar tiempo    

      # Bucle interno para recorrer la lista de nodos y buscar coincidencias
      while actual:
        if actual.patron.cadena_patron == self.primero.patron.cadena_patron:
          temp_tiempos+=(str(actual.patron.tiempo))+","  # Agrega el tiempo a la lista temporal
          # Si no hay nodo siguiente, elimina el primer nodo
        actual=actual.siguiente
      # Terminamos la iteración, quiere decir que ya tenemos la coincidencias:
      buffer=""

      #print(temp_tiempos)
      for digito in temp_tiempos:
        if digito.isdigit():
          buffer+=digito
        #Quiere decir que viene una coma
        else:
          if buffer!="":
            self.eliminar(int(buffer))
            buffer=""
          else:
            buffer=""

      resultado+=temp_tiempos+"--"
    return resultado  # Devuelve el resultado final con la agrupación de tiempos
