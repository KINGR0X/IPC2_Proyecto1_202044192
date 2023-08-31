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

    # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    # actual=self.primero
    # frecuencia=""
    # # while para recorrer los nodos
    # while actual != None:

    #   #for para recorrer cada caracter de la cadena
    #   for i in range(len(actual.grupo.cadena_grupo)):
    #     # se guardan los strings hasta encontrar una coma
    #     if actual.grupo.cadena_grupo[i]!=",":
    #       frecuencia+=actual.grupo.cadena_grupo[i]
    #     else:
    #       print(frecuencia)
    #       frecuencia=""
    #   actual=actual.siguiente
    # print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

  # graficar la lista de grupos
  def graficar(self, nombre_signal,amplitud):
        # f = open('bb.dot', 'w')
        # variable que conmtiene la configuración del grafo
        # se crea el subgrafo primero
    text="""
digraph G {
subgraph {
nodo_00[label=" """+nombre_signal+""" ",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_01_left[label="Amplitud\\n"""+amplitud+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_01_left;
}

fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]
a0 [shape=none label=<
<TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">
      """
    
    actual = self.primero
    sentinela_de_filas = actual.grupo.el_grupo  # iniciaria en 1, verifica si se cambio de linea
    fila_iniciada = False # para saber si se inicio una nueva fila
    frecuencia=""
    contador=0

    while actual != None:

      # si el_grupo es difrente al que viene entonces se cierra la fila
      if sentinela_de_filas != actual.grupo.el_grupo:
        sentinela_de_filas = actual.grupo.el_grupo
        # aun no se inicia una nueva fila por lo que es False
        fila_iniciada = False
        # Cerramos la fila
        text += """</TR>\n"""
        
      # si la fila iniciada es Fasle es porque se acaba de cerrar una fila, entonces inicializamos la nueva fila
      if fila_iniciada == False:
        # Se crea el nodo con el nombre del grupo
        contador+=1
        text+="""<TR>"""
        text += """<TD border="3"  bgcolor="yellow" gradientangle="315">"""+"""G="""+str(contador)+"""("""+str(actual.grupo.el_grupo[:-1])+""")"""+"""</TD>\n"""
        fila_iniciada = True
        # Abrimos la fila
        # for para obtener cada frecuencia
        for i in range(len(actual.grupo.cadena_grupo)):
          # se guardan los strings hasta encontrar una coma
          if actual.grupo.cadena_grupo[i]!=",":
            frecuencia+=actual.grupo.cadena_grupo[i]
          else:
            text += """<TD border="3"  bgcolor="yellow" gradientangle="315">""" + \
              frecuencia+"""</TD>\n"""
          #se vacia frecuencia porque ya se guardo en text
            frecuencia=""
            
      # Si no se da ninguno de los csos anteriores entonces secagrega una grupo con el TD
      else:
        # for para obtener cada frecuencia
        for i in range(len(actual.grupo.cadena_grupo)):
          # se guardan los strings hasta encontrar una coma
          if actual.grupo.cadena_grupo[i]!=",":
            frecuencia+=actual.grupo.cadena_grupo[i]
          else:
            text += """<TD border="3"  bgcolor="yellow" gradientangle="315">""" + \
              frecuencia+"""</TD>\n"""
          #se vacia frecuencia porque ya se guardo en text
            frecuencia=""

      actual = actual.siguiente

    # al fiunalizar el while se cierra la tablas
    text += """
</TR></TABLE>>];
}        
"""
    return text
  

  # Obtener_cada_string_del_grupo
  def obtener_cada_string_del_grupo(self):
    actual=self.primero
    frecuencia=""
    # while para recorrer los nodos
    while actual != None:

      for i in range(len(actual.grupo.cadena_grupo)):
        # se guardan los strings hasta encontrar una coma
        if actual.grupo.cadena_grupo[i]!=",":
          frecuencia+=actual.grupo.cadena_grupo[i]
        else:
          print(frecuencia)
          frecuencia=""
      actual=actual.siguiente
