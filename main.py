import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from signall import signall
from lista_signals import lista_signals
from lista_datos import lista_datos
from dato import dato
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
import os

# Recuperar el xml
ruta = askopenfilename()
archivo = open(ruta, "r")
archivo.close()

# Parsear para poder leer el xml
tree = ET.parse(ruta)
# se obtiene la raiz del xml
raiz = tree.getroot()

# ===== Lectura del xml =====
# Definimos una lista que guarde todas las signals
lista_signals_temporal = lista_signals()

# "senal" es elnombre de la equiqueta raiz
for signal_temporal in raiz.findall('senal'):

    # Obtener atributos principales (nombre, tiempo, amplitud)
    nombre_signal = signal_temporal.get('nombre')
    tiempo_signal = signal_temporal.get('t')
    amplitud_signal = signal_temporal.get('A')

    # Inicializamos listas temporales
    lista_datos_temporal = lista_datos()
    lista_datos_patrones_temporal = lista_datos()
    lista_patrones_temporal = lista_patrones()
    lista_grupos_temporal = lista_grupos()

    # se recorre cada linea del XML
    # se recorre cada dato que tiene la señal
    for dato_signal in signal_temporal.findall('dato'):
        tiempo_dato = dato_signal.get('t')
        amplitud_dato = dato_signal.get('A')
        # Con dato_signal.text se obtiene el "texto" que esta entre las etiquetas
        frecuencia_dato = dato_signal.text

        # creacion de un nuevo dato con los atributos obtenidos
        nuevo = dato(int(tiempo_dato), int(amplitud_dato), int(frecuencia_dato))

        #insertamos el objeto nuevo en la lista de datos
        lista_datos_temporal.insertar_dato(nuevo)
        
        # Inserción en lista_datos_patrones_temporal
        # Si no es un "0" entonces se guarda como un "1"
        if frecuencia_dato != "0":
            nuevo = dato(int(tiempo_dato), int(amplitud_dato), 1)
            lista_datos_patrones_temporal.insertar_dato(nuevo)
        else:
            nuevo = dato(int(tiempo_dato), int(amplitud_dato), 0)
            lista_datos_patrones_temporal.insertar_dato(nuevo)

    # Se guarda la lista de señales que hay en el XML     
    lista_signals_temporal.insertar_dato(signall(
        nombre_signal, tiempo_signal, amplitud_signal, lista_datos_temporal, lista_datos_patrones_temporal,lista_patrones_temporal,lista_grupos_temporal))    

    
# === funciones para generar las graficas ===

def generar_grafica_original(nombreGrafica):
        nombre = nombreGrafica+".dot"
        f = open(nombre, 'w')
         # se guara todo el texto y se cierra el archivo 
        f.write(str(lista_signals_temporal.grafica_mi_lista_original()))
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' 
        # se pasa el archivo a png
        os.system("""dot -Tpng """+nombre+""" -o """+nombreGrafica+""".png""")
        print("Grafica generada")


def generar_grafica_patrones(nombreGrafica):
        nombre = nombreGrafica+".dot"
        f = open(nombre, 'w')
         # se guara todo el texto y se cierra el archivo 
        f.write(str(lista_signals_temporal.grafica_mi_lista_de_patrones()))
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' 
        # se pasa el archivo a png
        os.system("""dot -Tpng """+nombre+""" -o """+nombreGrafica+""".png""")
        print("Grafica de patrones generada")


# lista_signals_temporal.recorrer_e_imprimir_lista()
lista_signals_temporal.calcular_los_patrones("Prueba 1")
# lista_signals_temporal.imprimir_nombre_signals()

# generar_grafica_original("Matriz")
# generar_grafica_patrones("MatrizPatrones")