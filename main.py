from libros import libros

# Definir la función que ordena una lista de libros por un campo específico (key) usando Merge Sort.
# Argumentos: libros (lista): La lista de libros a ordenar.
# key (str): El nombre de la clave por la cual se desea ordenar.
# Returns: lista: La lista de libros ordenada de forma ascendente.
def merge_sort_libros(libros, key):
    if len(libros) <= 1:
        return libros

    # Dividir la lista en dos mitades
    mid = len(libros) // 2
    mitad_izq = libros[:mid]
    mitad_der = libros[mid:]

    # Llamada recursiva para ordenar las mitades
    mitad_izq = merge_sort_libros(mitad_izq, key)
    mitad_der = merge_sort_libros(mitad_der, key)

    # Combinar las mitades ordenadas
    return merge(mitad_izq, mitad_der, key)


#Funcion que combina dos listas de libros ordenadas en una sola lista ordenada.
# Argumentos: izq (lista): La mitad izquierda de la lista ordenada.
# der (lista): La mitad derecha de la lista ordenada.
# key (str): La clave por la cual se están ordenando los diccionarios.
# Returns: lista: La lista combinada y ordenada.

def merge(izq, der, key):
   
    merged_lista = []
    i = 0  # Índice para la lista izquierda
    j = 0  # Índice para la lista derecha

    while i < len(izq) and j < len(der):
        if izq[i][key] <= der[j][key]:
            merged_lista.append(izq[i])
            i += 1
        else:
            merged_lista.append(der[j])
            j += 1

    # Agregar los elementos restantes de cualquiera de las listas
    while i < len(izq):
        merged_lista.append(izq[i])
        i += 1
    while j < len(der):
        merged_lista.append(der[j])
        j += 1

    return merged_lista

from libros import libros

# Ordenar por título
catalogo_ordenado_por_titulo = merge_sort_libros(libros, key="titulo")
print("Catálogo ordenado por título:")
for libro in catalogo_ordenado_por_titulo:
     print(f"  Título: {libro['titulo']}, Autor: {libro['autor']}")

print("\n" + "-"*30 + "\n")

# # Ordenar por autor
# catalogo_ordenado_por_autor = merge_sort_libros(libros, key="autor")
# print("Catálogo ordenado por autor:")
# for libro in catalogo_ordenado_por_autor:
#      print(f"  Autor: {libro['autor']}, Título: {libro['titulo']}")

# # # Ordenar por ISBN
# catalogo_ordenado_por_isbn = merge_sort_libros(libros, key="isbn")
# print("Catálogo ordenado por ISBN:")
# for libro in catalogo_ordenado_por_isbn:
#      print(f"  ISBN: {libro['isbn']}, Título: {libro['titulo']}")

# # # Ordenar por año
# catalogo_ordenado_por_anio = merge_sort_libros(libros, key="anio")
# print("Catálogo ordenado por año:")
# for libro in catalogo_ordenado_por_anio:
#      print(f"  Año: {libro['anio']}, Título: {libro['titulo']}")


#BUSQUEDA BINARIA CON VALIDACION MAYUS/MINUS Y ERROR CUANDO NO LO ENCUENTRA
def busqueda_binaria(lista, key, valor_busqueda):
    # Convertimos el valor de búsqueda a minúsculas .lower() y sin espacios .strip()para la comparación.
    valor_busqueda_lower = str(valor_busqueda).lower().strip()
    if len(lista) == 0:
        return "Valor no encontrado"
    medio = len(lista) // 2
    valor_central = lista[medio][key]
    # Convertimos el valor central del diccionario a minúsculas y sin espacios.
    valor_central_lower = str(valor_central).lower().strip()

    if valor_central_lower == valor_busqueda_lower:
        # Si lo encontramos, devolvemos el diccionario completo (no solo imprimir)
        # Esto hace la función más reutilizable.
        return lista[medio]
    else:
        if valor_busqueda_lower < valor_central_lower:
            return busqueda_binaria(lista[:medio], key, valor_busqueda)
        else:
            return busqueda_binaria(lista[medio + 1:], key, valor_busqueda)

#PRUEBAS DE BUSQUEDA
print("Pruebas de Búsqueda Binaria")
opciones = {
    "1": "titulo",
    "2": "autor",
    "3": "isbn",
    "4": "anio"
}

entrada = input("Ingrese el número correspondiente al criterio de búsqueda del libro: \n1. Titulo \n2. Autor \n3. ISBN \n4. Año \n ")
key_de_orden = opciones.get(entrada)
if key_de_orden is None:
    print("No ha ingresado un código correcto")
catalogo_ordenado = merge_sort_libros(libros, key=key_de_orden)
libro_a_buscar = str(input(f"ingrese el {key_de_orden} del libro que desea buscar"))
libro_encontrado_rec = busqueda_binaria(catalogo_ordenado, key_de_orden, libro_a_buscar)
if isinstance(libro_encontrado_rec, dict): # Si devuelve un diccionario, lo encontró
     print(f"\nLibro encontrado de'{libro_a_buscar}':")
     for k, v in libro_encontrado_rec.items():
        print(f"  {k}: {v}") 
else: # Si devuelve la cadena "Valor no encontrado"
     print(f"\nResultado de la búsqueda recursiva para '{libro_a_buscar}': {libro_encontrado_rec}")
