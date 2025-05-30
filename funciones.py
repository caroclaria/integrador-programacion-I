#busqueda
#lineal
#faltaria validar en mayus/minus y cartel de error cuando no se encuentre

def busqueda_lineal(lista,key,valor_busqueda):
    for i in range (len(lista)):
        if lista[i][key] == valor_busqueda:
            for key, valor in lista[i].items():
                print(f"{key}:{valor}")



#busqueda binaria
#debe estar previamente ordenado
def busqueda_binaria(lista, key, valor_busqueda):
    if len(lista) <= 0:
        return "Valor no encontrado"
    medio = len(lista)//2
    valor_central = lista[medio][key]
    if valor_central == valor_busqueda:
        for key, valor in lista[medio].items():
                print(f"{key}:{valor}")
    else:
         if valor_busqueda < valor_central:
              return busqueda_binaria(lista[:medio],key, valor_busqueda)
         else:
              return busqueda_binaria(lista[medio +1:],key, valor_busqueda)
        

