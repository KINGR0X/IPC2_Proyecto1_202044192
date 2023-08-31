from nodo_signal import nodo_signal
from grupo import grupo
import xml.etree.ElementTree as ET


class lista_signals:
    def __init__(self):
        self.primero = None
        self.contador_signals = 0

    def insertar_dato(self, signal):
        if self.primero is None:
            self.primero = nodo_signal(signal=signal)
            self.contador_signals += 1
            return

        # variable temporal para recorrer nuestra lista
        actual = self.primero

        # Con el while mientras actual.siguiente tenga un nodo al que apunta siguiente entonces se ejecuta el ciclo
        while actual.siguiente:
            actual = actual.siguiente

        # cuando el while termina es porque se llego al ultimo nodo, entonces se inserta el nuevo nodo
        actual.siguiente = nodo_signal(signal=signal)
        self.contador_signals += 1

    def recorrer_e_imprimir_lista(self):
        print("Total de carceles almacenadas:", self.contador_signals)
        print("")
        print("")
        print("")
        print("******************************************************************")
        actual = self.primero
        while actual != None:
            print("Nombre:", actual.signall.nombre, "Tiempo:", actual.signall.tiempo,
                  "Amplitud:", actual.signall.amplitud)

            actual.signall.lista_datos.recorrer_e_imprimir_lista()
            print("=== Lista Patrones ===")
            actual.signall.lista_patrones_datos.recorrer_e_imprimir_lista()

            actual = actual.siguiente
            print("")
            print("")
            print("")
        print("Numero de señales:", self.contador_signals)
        print("******************************************************************")
        print("")
        print("")
        print("")

    def calcular_los_patrones(self,nombre_signal):
        # recorremos la lista de signals hasta encontrar una coincidencia
        actual = self.primero
        while actual != None:
        # Si entra al if, es por que encontramos la signall que queremos
            if actual.signall.nombre==nombre_signal: 
                # Obtenemos sus patrones
                actual.signall.lista_patrones_tiempo=actual.signall.lista_patrones_datos.devolver_patrones_por_tiempo(actual.signall.lista_patrones_tiempo)
                # Imprimimos todos sus patrones
                actual.signall.lista_patrones_tiempo.recorrer_e_imprimir_lista()
                # obtenemos los grupos
                lista_patrones_temporal=actual.signall.lista_patrones_tiempo
                grupos_sin_analizar=lista_patrones_temporal.encontrar_coincidencias()
                # Este es un string, por ejemplo "1,2--3,5--4"
                print(grupos_sin_analizar)
                # por cada grupo recorrer la matriz original e ir devolviendo las coordenadas especificadas
                #recordando que por cada coincidencia encontrada, se va borrando para dejar solo las que no tienen grupo.
                buffer=""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito==",":
                        buffer+=digito
                    elif digito =="-" and buffer!="":
                        cadena_grupo=actual.signall.lista_datos.devolver_cadena_del_grupo(buffer)
                        actual.signall.lista_grupos.insertar_dato(grupo=grupo(buffer,cadena_grupo))
                        buffer=""
                    else:
                        buffer=""
                actual.signall.lista_grupos.recorrer_e_imprimir_lista()

                return
            actual=actual.siguiente
        print ("No se encontró la signall")


    # def imprimir_nombre_signals(self):
    #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    #     actual = self.primero
    #     while actual != None:
    #         print(actual.signall.nombre)
    #         actual = actual.siguiente
    #     print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # graficar mi_lista_original colocando el nombre de la señal
    def graficar_mi_lista_original(self, nombre_signal):
        actual = self.primero
        while actual != None:
            if actual.signall.nombre == nombre_signal:
                dot = actual.signall.lista_datos.graficar(actual.signall.nombre,
                                                           str(actual.signall.tiempo),
                                                           str(actual.signall.amplitud))
                # actual.signal.lista_patrones_dato.recorrer_e_imprimir_lista()
                return dot
            actual = actual.siguiente

    # graficar lista_patrones_datos colocando el nombre de la señal
    def graficar_lista_reducida(self, nombre_signal):
        actual = self.primero
        while actual != None:
            if actual.signall.nombre == nombre_signal:
                dot = actual.signall.lista_grupos.graficar(actual.signall.nombre,str(actual.signall.amplitud))
                # actual.signal.lista_patrones_dato.recorrer_e_imprimir_lista()
                return dot
            actual = actual.siguiente

    #Generar XML de salida
    def generar_xml_salida(self):
        actual=self.primero
        contador=0
        # creación del xml de salida
        mis_carceles=ET.Element("SenalesReducidas")
        # Crear un sub elemento <ListaCarceles> que le pertenezca a <misCarceles>
        lista_carceles=ET.SubElement(mis_carceles,"senal nombre="+"\""+actual.signall.nombre+"\""+" A="+"\""+actual.signall.amplitud+"\"")

        # El while es para graficar cada signal
        while actual!=None:

            actual_lista_patrones=actual.signall.lista_grupos.primero

            #while para recorrrer todos los grupos
            while actual_lista_patrones!=None:

                contador+=1
                # Crear un sub elemento <Carcel> que le pertenezca a <listaCarceles>
                signall=ET.SubElement(lista_carceles,"Grupo g="+"\""+str(contador)+"\"")
                # Crear un sub elemento <nombre> que le pertenezca a <Carcel>
                nombre=ET.SubElement(signall,"tiempos")
                nombre.text=actual_lista_patrones.grupo.el_grupo[:-1]
                # Recorremos la lista patrones (0 y 1) de la signall
                lista_patrones=ET.SubElement(signall,"datosGrupo")
                
                frecuencia=""
                # ciclo for para separar cada numero del string de grupo
                for i in range(len(actual_lista_patrones.grupo.cadena_grupo)):
                    # se guardan los strings hasta encontrar una coma
                    if actual_lista_patrones.grupo.cadena_grupo[i]!=",":
                        frecuencia+=actual_lista_patrones.grupo.cadena_grupo[i]
                    else:
                        dato=ET.SubElement(lista_patrones,"dato A="+"\""+str(i)+"\"")
                        dato.text=str(frecuencia)
                        frecuencia=""
                    
                actual_lista_patrones=actual_lista_patrones.siguiente

            actual=actual.siguiente

            #Generar xml
            my_data=ET.tostring(mis_carceles)
            my_data=str(my_data)
            self.xml_arreglado(mis_carceles)

            arbol_xml=ET.ElementTree(mis_carceles)
            arbol_xml.write("./Salida_XML/reportes/salida.xml",encoding="UTF-8",xml_declaration=True)
        print("XML generado")
        

    def xml_arreglado(self, element, indent='  '):
        # Inicializar una cola con el elemento raíz y nivel de anidación 0
        queue = [(0, element)]  # (level, element)
        # Bucle principal: continúa mientras haya elementos en la cola
        while queue:
            # Extraer nivel y elemento actual de la cola
            level, element = queue.pop(0)
            # Crear tuplas para cada hijo con nivel incrementado
            children = [(level + 1, child) for child in list(element)]
            # Agregar saltos de línea e indentación al inicio del elemento actual
            if children:
                element.text = '\n' + indent * (level + 1)
                # Agregar saltos de línea e indentación al final del elemento actual
            if queue:
                element.tail = '\n' + indent * queue[0][0]
            else:
                # Si este es el último elemento del nivel actual, reducir la indentación
                element.tail = '\n' + indent * (level - 1)
            # Insertar las tuplas de hijos al principio de la cola
            queue[0:0] = children
