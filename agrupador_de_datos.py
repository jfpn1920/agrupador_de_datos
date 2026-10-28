ids = []
nombres = []
categorias = []
tipos = []
valores = []
fechas = []
descripciones = []
#---------------------------------------#
#--|menu_principal_agrupador_de_datos|--#
#---------------------------------------#
while True:
    print("menu principal agrupador de datos")
    print("1) crear dato")
    print("2) editar dato")
    print("3) eliminar dato")
    print("4) buscar dato")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------#
    #--|crear_dato|--#
    #----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_dato = 1
        else:
            id_dato = ids[-1] + 1
        nombre = input("nombre del dato: ")
        categoria = input("categoría: ")
        tipo = input("tipo: ")
        valor = float(input("valor: "))
        fecha = input("fecha: ")
        descripcion = input("descripción: ")
        ids.append(id_dato)
        nombres.append(nombre)
        categorias.append(categoria)
        tipos.append(tipo)
        valores.append(valor)
        fechas.append(fecha)
        descripciones.append(descripcion)
        print("dato registrado correctamente.")
        print("id:", id_dato)
    #-----------------#
    #--|editar_dato|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar dato")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {tipos[i]} | {valores[i]} | {fechas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {valores[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
                nombres[posicion] = input("nuevo nombre del dato: ")
                categorias[posicion] = input("nueva categoría: ")
                tipos[posicion] = input("nuevo tipo: ")
                valores[posicion] = float(input("nuevo valor: "))
                fechas[posicion] = input("nueva fecha: ")
                descripciones[posicion] = input("nueva descripción: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_dato|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar dato")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {tipos[i]} | {valores[i]} | {fechas[i]} | {descripciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {valores[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    categorias.pop(posicion)
                    tipos.pop(posicion)
                    valores.pop(posicion)
                    fechas.pop(posicion)
                    descripciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_dato|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar dato")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {categorias[posicion]} | {tipos[posicion]} | {valores[posicion]} | {fechas[posicion]} | {descripciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            suma = 0
            mayor = valores[0]
            menor = valores[0]
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {tipos[i]} | {valores[i]} | {fechas[i]} | {descripciones[i]}")
                suma += valores[i]
                if valores[i] > mayor:
                    mayor = valores[i]
                if valores[i] < menor:
                    menor = valores[i]
            promedio = suma / len(ids)
            print("estadísticas agrupador de datos")
            print("cantidad de registros:", len(ids))
            print("valor acumulado:", round(suma, 2))
            print("valor promedio:", round(promedio, 2))
            print("mayor valor:", round(mayor, 2))
            print("menor valor:", round(menor, 2))
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el agrupador de datos.")
        break
    else:
        print("opción no válida.")