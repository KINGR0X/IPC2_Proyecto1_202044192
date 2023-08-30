from nodo_grupo import nodo_grupo

class lista_grupos:
  def __init__(self):
    self.primero = None
    self.contador_grupos=0


  def insertar_dato(self,grupo):
    if self.primero is None:
      self.primero = nodo_grupo(grupo=grupo)
      self.contador_grupos+=1
      return
    actual= self.primero
    while actual.siguiente:
      actual = actual.siguiente
    actual.siguiente = nodo_grupo(grupo=grupo)
    self.contador_grupos+=1

  def recorrer_e_imprimir_lista(self):
    print("===========================================================================================")
    actual = self.primero
    while actual != None:
      print("Grupo: ",actual.grupo.el_grupo,"Cadena-grupo: ",actual.grupo.cadena_grupo)
      actual = actual.siguiente
    print("===========================================================================================")

  #obtner el tamño de la cadena antes del salto de linea
  def obtener_amplitud(self):
    actual=self.primero
    size_cadena= 0
    
    for i in range(len(actual.grupo.cadena_grupo)):
      #si es una coma no se cuenta
      if actual.grupo.cadena_grupo[i]!="\n":
        size_cadena+=1
      else:
        break
    
    print("la amplitud es de:",size_cadena)
    print("la cadena es de:",len(actual.grupo.cadena_grupo))
    return size_cadena


  # # sumar cadena_grupo de cada grupo
  # def sumar_cadena_grupo(self):
  #   string_resultado=""
  #   string_temporal=""
  #   actual = self.primero
  #   amplitud=self.obtener_amplitud()
  #   #se recorren todos los nodos
  #   while actual != None:
  #     # se suma lo de la derecha del salto de linea con lo de la izquierda del salto de linea, ej: "2,3,X,5,8"
  #     # da como resultado "7,11"
  #     for i in range(len(actual.grupo.cadena_grupo)):

  #       string_temporal+=str(int(actual.grupo.cadena_grupo[i-1])+ int(actual.grupo.cadena_grupo[amplitud+1])) 

  #     actual = actual.siguiente



