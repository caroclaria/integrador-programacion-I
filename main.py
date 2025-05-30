from libros import libros
from funciones import busqueda_lineal, busqueda_binaria

print(busqueda_lineal(libros,"titulo","Orgullo y prejuicio"))


lista_ordenada = sorted(libros, key=lambda x: x["titulo"])
busqueda_binaria(lista_ordenada, "titulo", "Orgullo y prejuicio")
