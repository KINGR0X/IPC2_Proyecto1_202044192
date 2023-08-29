class signall:
    # Una señal segun el enunciado debe de tener lo enlistado en el init
    def __init__(self, nombre, tiempo, amplitud, lista_datos, lista_patrones_datos,lista_patrones_tiempo,lista_grupos):
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.lista_datos = lista_datos
        self.lista_patrones_datos = lista_patrones_datos
        # lsitas con los mismos patrones en la lista reducida (lista_patrones_datos)
        self.lista_patrones_tiempo = lista_patrones_tiempo
        # lsita donde se agrupan las filas con los mismps patrones (lista_patrones_tiempo)
        self.lista_grupos = lista_grupos
