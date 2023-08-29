from nodo_signal import nodo_signal
from grupo import grupo


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
        # recorremos la lista de carceles hasta encontrar una coincidencia
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


    def imprimir_nombre_signals(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        actual = self.primero
        while actual != None:
            print(actual.signall.nombre)
            actual = actual.siguiente
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    # def grafica_mi_lista_original(self):
    #     actual = self.primero
    #     while actual != None:
    #         dot = actual.signall.lista_datos.graficar(actual.signall.nombre,
    #                                                    str(actual.signall.tiempo),
    #                                                    str(actual.signall.amplitud))
    #         # actual.signal.lista_patrones_dato.recorrer_e_imprimir_lista()
    #         actual = actual.siguiente

        # return dot

    def grafica_mi_lista_de_patrones(self):
        actual = self.primero
        while actual != None:
            dot= actual.signall.lista_patrones_datos.graficar(actual.signall.nombre,
                                                                str(actual.signall.tiempo),
                                                                str(actual.signall.amplitud))
            # actual.signal.lista_patrones_dato.recorrer_e_imprimir_lista()
            actual = actual.siguiente

        return dot

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
