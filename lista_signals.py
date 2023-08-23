from nodo_signal import nodo_signal


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
        print("******************************************************************")
        print("")
        print("")
        print("")

    # def grafica_mi_lista_original(self):
    #     actual = self.primero
    #     while actual != None:
    #         actual.signal.lista_celdas.generar_grafica(actual.signal.nombre,
    #                                                    str(actual.signal.niveles),
    #                                                    str(actual.signal.celdas_por_nivel))
    #         # actual.signal.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #         actual = actual.siguiente

    # def grafica_mi_lista_de_patrones(self):
    #     actual = self.primero
    #     while actual != None:
    #         actual.signal.lista_patrones_celdas.generar_grafica(actual.signal.nombre,
    #                                                             str(actual.signal.niveles),
    #                                                             str(actual.signal.celdas_por_nivel))
    #         # actual.signal.lista_patrones_celdas.recorrer_e_imprimir_lista()
    #         actual = actual.siguiente
