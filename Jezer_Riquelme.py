def mostrarMenu():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")

def leer_opcion():
    while True:
        try:
            opcion=int(input("Ingrese la opcion a realizar: "))
            if opcion > 0 and opcion <=6:
                return opcion
            else:
                print("Debe ingresar una opcion valida (1-6).")
        except ValueError:
            print("Debe ser una opcion valida.")

def cupos_tipo(tipoBuscado, diccionarioplanes, diccionarioinscripciones):
    tipoBuscado=tipoBuscado.strip().lower()
    acumulador_plan=0
    for codigo_cupos, lista_inscripciones in diccionarioplanes.items():
        lista_inscripciones[1] == tipoBuscado
        for codigo_inscripciones, lista_atributos_inscripciones in diccionarioinscripciones.items():
            if codigo_cupos==codigo_inscripciones:
                acumulador_plan += lista_atributos_inscripciones[1]
                break
    print(f"el total de cupos {acumulador_plan} ")

def busqueda_precio(p_min, p_max, diccionarioinscripciones, diccionarioplanes):
    lista_planes=[]
    for codigo_inscipciones, lista_atributos_incripciones, in diccionarioinscripciones.items():
        if lista_atributos_incripciones[0] >= p_min and lista_atributos_incripciones[0] <= p_max and lista_atributos_incripciones[1] > 0:
            for codigo_plan, lista_atributos in diccionarioplanes.items():
                if codigo_inscipciones == codigo_plan:
                    lista_planes.append(f"{lista_atributos[0]} -- {codigo_inscipciones}")
                    break
    if len(lista_planes) == 0:
        print("No hay planes en ese rango de precios.")
    else:
        lista_planes.sort()
        for plan in lista_planes:
            print(plan)

def buscar_codigo(codigo, diccionarioinscripciones):
    for codigo_inscripciones in diccionarioinscripciones.keys():
        if codigo == codigo_inscripciones:
            return True
    return False

def actualizar_precio(codigo, nuevo_precio, diccionarioinscripciones):
    if buscar_codigo(codigo, diccionarioinscripciones) == True:
        lista_atributos=diccionarioinscripciones[codigo]
        lista_atributos[0]=nuevo_precio
        return True
    else:
        return False
    
def validar_codigo(codigo):
    return codigo.strip() != "" and codigo not in planes

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_tipo(tipo):
    return tipo.lower() in ["mensual", "trimestral","anual"]

def validar_duracion(duracion):
    return duracion.isdigit() and  int(duracion) > 0

def validar_sn(valor):
    return valor.lower() in ["s","n"]

def validar_horario(horario):
    return horario.strip() != ""

def validar_precio(precio):
    return precio.isdigit() and int(precio) >0

def validar_cupos(cupos):
    return cupos.isdigit() and int(cupos) >= 0

def agregar_plan(lista):

    codigo=input(" Ingrese código del plan: ")
    nombre=input(" Ingrese nombre del plan: ")
    tipo=input (" Ingrese tipo (mensual/trimestral/anual): ")
    duracion =input("Ingrese duración (meses): ")
    acceso_piscina=input("Ingrese duración (meses): ")
    incluye_clases =input ("¿Incluye clases grupales? (s/n): ")
    horario =input("Ingrese horario: ")
    precio = input (" Ingrese precio: ")
    cupos =input(" Ingrese cupos: ")

    codigoValido=validar_codigo(codigo)
    nombreValido=validar_nombre(nombre)
    tipoValido = validar_tipo(tipo)
    duracionValido =validar_duracion(duracion)
    horarioValido=validar_horario(horario)
    precioValido=validar_precio(precio)
    cuposValido=validar_cupos(cupos)

    if codigoValido == True and nombreValido == True and tipoValido == True and duracionValido == True and horarioValido == True and precioValido == True and cuposValido == True:
        planes[codigo] = {
            "nombre": nombre,
            "tipo": tipo, 
            "duracion": duracion,
            "acceso_piscina":acceso_piscina,
            "incluye_clases": incluye_clases,
            "horario":horario,
            "precio": precio, 
            "cupos": cupos
        }
        inscripciones[codigo] =[]
    else: 
        print("Error, los datos no son validos")
        


def eliminar_plan(codigo_buscado, diccionarioplanes, diccionarioincripciones):
    if buscar_codigo(codigo_buscado, diccionarioplanes):
        del diccionarioplanes[codigo_buscado]
        del diccionarioincripciones[codigo_buscado]
        return True
    else:
        return False

planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}

inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}

while True:
    mostrarMenu()
    opcionSeleccionada=leer_opcion()

    if opcionSeleccionada == 1:
        tipo_buscado=input("Ingrese el tipo de plan a consultar: ")

        cupos_tipo(tipo_buscado, planes, inscripciones)
    elif opcionSeleccionada == 2:
        while True:
            try:
                precio_minimo=int(input("Ingrese el precio minimo del rango: "))
                precio_maximo=int(input("Ingrese el precio maximo del rango: "))
                if precio_minimo < 0 or precio_minimo > precio_maximo:
                    print("Debe ingresar valores enteros positivos mayor que cero, el rango debe ser menor al rango maximo")
                else:
                    busqueda_precio(precio_minimo, precio_maximo, inscripciones, planes)
                    break
            except ValueError:
                print("Debe ingresar valores enteros")
    elif opcionSeleccionada == 3:
        while True:
            codigo_buscado=input("Ingrese el codigo del arreglo o actualizar: ")
            while True:
                try:
                    precio_nuevo=int(input("Ingrese el precio nuevo: "))
                    if precio_nuevo <= 0:
                        print("Debe ingresar valores enteros positivos")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar valores enteros positivos. ")
            actualizado=actualizar_precio(codigo_buscado, precio_nuevo, inscripciones)
            if actualizado == True:
                print("Precio actualizado")
            else:
                print("Codigo no existe")
            otro_precio=input("Desea actualizar otro precio (S/N)? ")
            if otro_precio == 's':
                continue
            else:
                break
    elif opcionSeleccionada == 4:
        agregar_plan(planes)
    elif opcionSeleccionada == 5:
        codigo_eliminar=input("Ingrese el codigo a eliminar: ")
        eliminado=eliminar_plan(codigo_eliminar, planes, inscripciones)
        if eliminado == True:
            print("Plan eliminado. ")
        else:
            print("El codigo no existe")
    elif opcionSeleccionada == 6:
        print("Programa finalizado.")

                                     