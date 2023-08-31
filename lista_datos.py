from nodo_dato import nodo_dato
import os
from patron import patron


class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos = 0

    def insertar_dato(self, dato):
        # Si el primer nodo es nulo entonces el nodo que se inserta es el primero
        if self.primero is None:
            self.primero = nodo_dato(dato=dato)
            self.contador_datos += 1
            return

        # variable temporal para recorrer nuestra lista
        actual =self.primero

        # Con el while mientras actual.siguiente tenga un nodo al que apunta siguiente entonces se ejecuta el ciclo
        while actual.siguiente:
            actual = actual.siguiente

        # cuando el while termina es porque se llego al ultimo nodo, entonces se inserta el nuevo nodo
        actual.siguiente = nodo_dato(dato=dato)
        self.contador_datos += 1

    def recorrer_e_imprimir_lista(self):
        # print("el primer dato es:",self.primero.dato.tiempo, self.primero.dato.amplitud, self.primero.dato.frecuencia)
        print("============================================================")
        actual = self.primero
        # actual empieza desde el primer nodo ingresado, y va recorriendo el resto de nodos, hasta que ya no queden nodos
        while actual != None:
            print("Tiempo:", actual.dato.tiempo, "Amplitud:", actual.dato.amplitud,
                  "frecuencia:", actual.dato.frecuencia)
            actual = actual.siguiente
        print("============================================================")


    def graficar(self, nombre_signal, tiempo, amplitud):
        # f = open('bb.dot', 'w')
        # variable que conmtiene la configuración del grafo
        # se crea el subgrafo primero
        text="""
digraph G {
subgraph {
nodo_00[label=" """+nombre_signal+""" ",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_01_left[label="Tiempo\\n"""+tiempo+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_01_left;
nodo_01_right[label="Amplitud\\n"""+amplitud+"""",fontcolor="#000000",fillcolor=gold, style=filled,shape=box];
nodo_00 -> nodo_01_right;
}

fontname="Helvetica,Arial,sans-serif"
node [fontname="Helvetica,Arial,sans-serif"]
edge [fontname="Helvetica,Arial,sans-serif"]
a0 [shape=none label=<
<TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">
            """

        actual = self.primero
        sentinela_de_filas = actual.dato.tiempo  # iniciaria en 1, verifica si se cambio de linea
        fila_iniciada = False # para saber si se inicio una nueva fila

        while actual != None:
            # Si mi fila actual es diferente a la que viene, ej: t=1 y el siguiente es t=2
            if sentinela_de_filas != actual.dato.tiempo:
                sentinela_de_filas = actual.dato.tiempo
                # aun no se inicia una nueva fila por lo que es False
                fila_iniciada = False
                # Cerramos la fila
                text += """</TR>\n"""

            # si la fila iniciada es Fasle es porque se acaba de cerrar una fila, entonces inicializamos la nueva fila
            if fila_iniciada == False:
                fila_iniciada = True
                # Abrimos la fila
                text += """<TR>"""
                text += """<TD border="3"  bgcolor="yellow" gradientangle="315">""" + \
                    str(actual.dato.frecuencia)+"""</TD>\n"""
            
            # Si no se da ninguno de los csos anteriores entonces secagrega una dato con el TD
            else:
                text += """<TD border="3"  bgcolor="yellow" gradientangle="315">""" + \
                    str(actual.dato.frecuencia)+"""</TD>\n"""
            actual = actual.siguiente

        # al fiunalizar el while se cierra la tablas
        text += """
</TR></TABLE>>];
}        
"""
        return text

    def devolver_cadena_del_grupo(self,grupo):
        string_resultado=""
        string_temporal=""
        buffer=""
        string_temporal2=""
        string_auxiliar=""
        contador=0
        # viene un parametro llamado grupo, es un string con este formato "1,3"
        # recorremos caracter por caracter
        for digito in grupo:
        #si es digito
            if digito.isdigit():
                #añadimos al buffer
                buffer+=digito
            else:
                # si no es buffer, lo vaciamos
                string_temporal=""
                string_temporal2=""
                string_resultado=""
                #recorremos *TODA* la lista y recuperamos los valores para este grupo
                actual = self.primero
                while actual != None:
                # si encontramos coincidencia del digito y el tiempo , obtenemos su valor

                    if actual.dato.tiempo==int(buffer) and len(string_auxiliar)!=0: #significa que ya se dio una vuelta
                        string_temporal2=str(actual.dato.frecuencia)
                        # se suma string_temporal con buffer2
                        string_temporal+=str(int(string_temporal2)+int(string_auxiliar[contador]))+","
                        contador+=2

                    elif actual.dato.tiempo==int(buffer):
                        string_temporal+=str(actual.dato.frecuencia)+","

                    actual = actual.siguiente
                    
                string_resultado+=string_temporal
                string_auxiliar=string_resultado
                buffer=""
                contador=0

        # # se elimina el inicio del strign que no se necesita
        # palabra= "2,3,0,4,5,7,0,6"
        # #imprimir desde el 5 hsta el 6
        # print(palabra[8:])

        #devolvemos el string resultado
        return string_resultado
    

    
  # método para devolver los patrones por tiempo
    def devolver_patrones_por_tiempo(self,lista_patrones_tiempo):
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo #iniciaria en 1
        fila_iniciada=False
        recolector_patron=""
        while actual != None:
        # si hay cambio de fila entramos al if
            if sentinela_de_filas!=actual.dato.tiempo:
                # fila iniciada se vuelve false, por que se acaba la fila
                fila_iniciada=False
                # ya que terminamos la fila, podemos guardar los patrones
                lista_patrones_tiempo.insertar_dato(patron(sentinela_de_filas,recolector_patron))
                recolector_patron=""
                # actualizamos el valor de la fila (tiempo)
                sentinela_de_filas=actual.dato.tiempo
            # si fila iniciada es false, quiere decir que acaba de terminar fila y debemos empezar una nueva
            if fila_iniciada==False:
                fila_iniciada=True
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.frecuencia)+"-"
            else:
                #Recolectamos el valor, ya que estamos en la fila
                recolector_patron+=str(actual.dato.frecuencia)+"-"
            actual = actual.siguiente
        # Agregamos un nuevo patrón, sería el de toda la fila, ej: 0-1-1-1
        lista_patrones_tiempo.insertar_dato(patron(sentinela_de_filas,recolector_patron))
        # devolvermos la lista llena con los patrones
        return lista_patrones_tiempo