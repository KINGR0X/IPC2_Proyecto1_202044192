from nodo_dato import nodo_dato
import sys
import os


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


    def generar_grafica(self, nombre_signal, tiempo, amplitud):
        f = open('bb.dot', 'w')
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
            
            # Si no se da ninguno de los csos anteriores entonces secagrega una celda con el TD
            else:
                text += """<TD border="3"  bgcolor="yellow" gradientangle="315">""" + \
                    str(actual.dato.frecuencia)+"""</TD>\n"""
            actual = actual.siguiente

        # al fiunalizar el while se cierra la tablas
        text += """
</TR></TABLE>>];
}        
"""
        
        # se guara todo el texto y se cierra el archivo 
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' 
        # se pasa el archivo a png
        os.system('dot -Tpng bb.dot -o grafo.png')
        print("Grafica generada")
