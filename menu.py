from colorama import init, Fore, Back, Style
# ====== Menú principal ======


def menu_prinicipal():
    print(Fore.YELLOW+"\n=== Menú principal ===".center(100))
    while True:
        print(Fore.WHITE+"\nSeleccione una opción del menú:")
        print("1.Cargar archivo")
        print("2.Procesar archivo")
        print("3.Escribir archivo salida")
        print("4.Mostrar datos del estudiante")
        print("5.Generar gráfica")
        print("6.Inicializar sistema")
        print("7.Salir")

        opcion = input("Opción seleccionada: ").strip()
        print(Fore.RESET)

        if opcion == "1":
            print("1.Cargar archivo")
        elif opcion == "2":
            print("2.Procesar archivo")
        elif opcion == "3":
            print("3.Escribir archivo salida")
        elif opcion == "4":
            print("4.Mostrar datos del estudiante")
        elif opcion == "5":
            print("5.Generar gráfica")
        elif opcion == "6":
            print("6.Inicializar sistema")
        elif opcion == "7":
            print("7.Salir")
            break
        else:
            print(Fore.RED+"Opción no válida. Por favor seleccione una opción del menú.")


menu_prinicipal()
