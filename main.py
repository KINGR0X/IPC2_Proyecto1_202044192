import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from signall import signall
from lista_signals import lista_signals
from lista_datos import lista_datos
from dato import dato
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos
import os
from colorama import init, Fore, Back, Style


# se establece lista_signals_temporal como una lista global
lista_signals_temporal=lista_signals()

def menu_prinicipal():
    print(Fore.YELLOW+"\n=== Menú principal ===".center(100))
    global ArchivoProcesado
    global graficado
    while True:
        print(Fore.YELLOW+"\n=== Seleccione una opción del menú ===")
        print(Fore.WHITE+"1.Cargar archivo")
        print("2.Procesar archivo")
        print("3.Escribir archivo salida")
        print("4.Mostrar datos del estudiante")
        print("5.Generar gráfica")
        print("6.Inicializar sistema")
        print("7.Salir")

        opcion = input("Opción seleccionada: ").strip()
        print(Fore.RESET)

        if opcion == "1":
            try:
                print(Fore.YELLOW+"=== Seleccione un archivo ===")
                lista_signals_temporal=cargar_archivo()
                print(Fore.GREEN+"Archivo cargado con exito")
            except:
                print(Fore.RED+"=== Error al cargar el archivo ===")
                menu_prinicipal()

        elif opcion == "2":

            try:
                ArchivoProcesado=True
                print(Fore.BLUE+"Leyendo el archivo de entrada...")
                print(Fore.BLUE+"Creando nodos...")
                print(Fore.BLUE+"Calculando patrones...")
                print(Fore.BLUE+"Creando grupos...")
                #se imprime el nombre de las señales procesadas

                # Se debe de llamar a cada señal del archivo por separado, para luego usarlo en la grafica
                actual = lista_signals_temporal.primero
                while actual != None:
                        lista_signals_temporal.calcular_los_patrones(str(actual.signall.nombre))
                        actual = actual.siguiente
                        
                print(Fore.GREEN+"Archivo procesado con exito")
            except:
                print(Fore.RED+"=== Error al procesar el archivo ===")
                menu_prinicipal()

        elif opcion == "3":

            if ArchivoProcesado==True:
                try:
                    print(Fore.YELLOW+"=== Seleccione una ubicación para el archivo de salida ===")
                    #se pide la dirección donde se guardará el archivo
                    direccion_archivo = filedialog.asksaveasfilename(defaultextension=".xml",
                                                                    filetypes=[("Archivos de texto", "*.xml"), ("Todos los archivos", "*.*")],
                                                                    title="Guardar archivo como", initialfile="Saida")

                    # Se debe de llamar a cada señal del archivo por separado
                    actual = lista_signals_temporal.primero
                    while actual != None:
                        lista_signals_temporal.calcular_los_patrones(str(actual.signall.nombre))
                        actual = actual.siguiente
                    lista_signals_temporal.generar_xml_salida(direccion_archivo)
                    print(Fore.GREEN+"Archivo de salida generado con exito")
                except:
                    print(Fore.RED+"=== Error al generar el archivo de salida ===")
                    menu_prinicipal()
            else:
                print(Fore.RED+"=== No se a procesado ningun archivo ===")
                menu_prinicipal()

        elif opcion == "4":
            print(Fore.YELLOW+"             ===== Datos del estudiante =====")
            print(Fore.YELLOW+"=============================================================")
            print(Fore.BLUE+"Carnet: 202044192")
            print(Fore.BLUE+"Nombre: Elian Angel Fernando Reyes Yac")
            print(Fore.BLUE+"Curso: Introducción a la Programación y Computación 2")
            print(Fore.BLUE+"Carrera: Ingeniería en Ciencias y Sistemas")
            print(Fore.BLUE+"Semestre: 2do Semestre 2023")
            print(Fore.YELLOW+"=============================================================")

        elif opcion == "5":

            if ArchivoProcesado==True:

                try:
                    print(Fore.YELLOW+"=== Ingrese el numero de la señal a graficar===")

                    #Funcionpara graficar las dos matrices a la vez
                    def generar_grafica_original(nombreSignal):
                        nombreGrafica= "Matriz_original"
                        nombre = nombreGrafica+".dot"
                        f = open(nombre, 'w')
                        # se guara todo el texto y se cierra el archivo 
                        f.write(str(lista_signals_temporal.graficar_mi_lista_original(nombreSignal)))
                        f.close()
                        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' 
                        # se pasa el archivo a png
                        os.system("""dot -Tpng """+nombre+""" -o """+nombreGrafica+""".png""")

                        # === grafica matriz reducida ===
                        nombreGraficaReducida= "Matriz_reducida"
                        nombreR = nombreGraficaReducida+".dot"
                        f = open(nombreR, 'w')
                        # se guara todo el texto y se cierra el archivo 
                        f.write(str(lista_signals_temporal.graficar_lista_reducida(nombreSignal)))
                        f.close()
                        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' 
                        # se pasa el archivo a png
                        os.system("""dot -Tpng """+nombreR+""" -o """+nombreGraficaReducida+""".png""")
                    
                    # === Imprimir las señales que hay en el archivo ===
                    actual = lista_signals_temporal.primero
                    contador=0
                    while actual != None:
                        contador+=1
                        print(Fore.WHITE+str(contador)+". "+actual.signall.nombre)
                        # lista_signals_temporal.calcular_los_patrones(str(actual.signall.nombre))
                        actual = actual.siguiente

                    # el usuario escoge un numero
                    numero_signal = input("Señal a graficar: ").strip()

                    # === convertir el numero seleccionado a el nombre de la señal ===
                    actual = lista_signals_temporal.primero
                    contadorAux=0
                    signal_a_graficar=""
                    while actual != None:
                        contadorAux+=1
                        if numero_signal == str(contadorAux):
                            signal_a_graficar=actual.signall.nombre
                            # lista_signals_temporal.calcular_los_patrones(str(actual.signall.nombre))
                        actual = actual.siguiente

                    # === Se calculan los patrones para graficar ===
                    # pero solo se calculan si no se han calculado antes (si no se han graficado ya)
                    # if graficado==False:
                    #     lista_signals_temporal.calcular_los_patrones(str(signal_a_graficar))
                    # #Generar grafica
                    generar_grafica_original(signal_a_graficar)
                    graficado=True
                    print(Fore.GREEN+"Graficas generadas con exito")

                except:
                    print(Fore.RED+"=== Error al generar las graficas ===")
                    menu_prinicipal()
            else:
                print(Fore.RED+"=== No se a procesado ningun archivo ===")
                menu_prinicipal()

        elif opcion == "6":
            try:
                print(Fore.YELLOW+"=== Inicializando sistema ===")
                #limpiar la lista
                lista_signals_temporal=lista_signals()
                print(Fore.GREEN+"Sistema inicializado con exito")
                ArchivoProcesado=False
            except:
                print(Fore.RED+"=== Error al inicializar el sistema ===")
                menu_prinicipal()

        elif opcion == "7":
            print("7.Salir")
            break
        else:
            print(Fore.RED+"Opción no válida. Por favor seleccione una opción del menú.")

 

def cargar_archivo():
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

    print(Fore.GREEN+"\n=== Archivo cargado ===".center(100))
    return lista_signals_temporal 
        

ArchivoProcesado=False
graficado=False
menu_prinicipal()
