stock_viernes = 150
stock_sabado = 180
nombres_viernes = ""
nombres_sabado = ""

while True:
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")

    opcion = input("Seleccione una opción: ")

    if opcion =="1":
        nombre = input("Ingrese nombre del comprador: ").strip()

        
        if ("," + nombre + ",") in ("," + nombres_viernes + ",") or ("," + nombre + ",") in ("," + nombres_sabado + ","):
            print("¡Error! Nombre ya registrado.")
        else:
            print("Seleccione función:")
            print("1. Cats Día Viernes")
            print("2. Cats Día Sábado")
            funcion = input("Ingrese número de función: ")

            if funcion == "1":
                if stock_viernes > 0:
                    stock_viernes -= 1
                    nombres_viernes += nombre + ","
                    print("Entrada registrada para función viernes.")
                else:
                    print("No hay stock para función viernes.")
            elif funcion == "2":
                if stock_sabado > 0:
                    stock_sabado -= 1
                    nombres_sabado += nombre + ","
                    print("Entrada registrada para función sábado.")
                else:
                    print("No hay stock para función sábado.")
            else:
                print("Función inválida.")

    elif opcion == "2":
        nombre = input("Ingrese nombre del comprador para cambiar de función: ").strip()

        esta_en_viernes = ("," + nombre + ",") in ("," + nombres_viernes + ",")
        esta_en_sabado = ("," + nombre + ",") in ("," + nombres_sabado + ",")

        if esta_en_viernes:
            if stock_sabado > 0:
                confirmacion = input("¿Desea cambiar a función sábado? (s/n): ").strip().lower()
                if confirmacion == "s":
                    
                    nueva_lista = ""
                    for n in nombres_viernes.split(","):
                        if n != "" and n != nombre:
                            nueva_lista += n + ","
                    nombres_viernes = nueva_lista
                    
                    nombres_sabado += nombre + ","
                    stock_viernes += 1
                    stock_sabado -= 1
                    print("Cambio realizado con éxito.")
                else:
                    print("Cambio cancelado.")
            else:
                print("No hay stock en función sábado.")

        elif esta_en_sabado:
            if stock_viernes > 0:
                confirmacion = input("¿Desea cambiar a función viernes? (s/n): ").strip().lower()
                if confirmacion == "s":
                    
                    nueva_lista = ""
                    for n in nombres_sabado.split(","):
                        if n != "" and n != nombre:
                            nueva_lista += n + ","
                    nombres_sabado = nueva_lista
                    
                    nombres_viernes += nombre + ","
                    stock_sabado += 1
                    stock_viernes -= 1
                    print("Cambio realizado con éxito.")
                else:
                    print("Cambio cancelado.")
            else:
                print("No hay stock en función viernes.")
        else:
            print("Nombre no encontrado.")

    elif opcion == "3":
        total_vendidos = (150 - stock_viernes) + (180 - stock_sabado)
        print("\n--- Totales ---")
        print("Entradas disponibles - Cats Día Viernes:", stock_viernes)
        print("Entradas disponibles - Cats Día Sábado:", stock_sabado)
        print("Total de entradas vendidas:", total_vendidos)

    elif opcion == "4":
        print("*Programa terminado...*")
        break

    else:
        print("*Debe ingresar una opción válida")




    
                





