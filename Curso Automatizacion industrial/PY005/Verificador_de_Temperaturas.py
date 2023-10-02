# Verificador de temperaturas:

# Hacer una función que tome, de una lista de valores, las temperaturas registradas en un día. De esa lista, debe retornar: 

# _Promedio de temperaturas
# _Temperatura más baja
# _Temperatura más alta
# _Cantidad de temperaturas menores a 22°c

# Hacer otra función que imprima los valores en un texto legible para el operador

import statistics as stats

Temperaturas1=[27.1, 22.3, 26.8, 23.5, 22.7, 15.3, 26.6, 16.9, 18.1, 24.7, 23.8, 18.4, 26.1, 27.5, 27.3, 21.9, 25.4, 25.1, 20.4, 16.2, 27.5, 22.7, 25.9, 21.2]
Temperaturas2=[25.4, 21.5, 27.3, 25.5, 20.2, 26.6, 16.1, 27.7, 26.4, 24.0, 22.6, 19.4, 27.0, 18.3, 25.0, 24.3, 25.6, 27.1, 15.6, 27.1, 26.6, 22.7, 20.4, 23.3]
Temperaturas3=[16.4, 20.5, 23.5, 17.3, 26.2, 26.2, 22.9, 21.2, 24.2, 26.0, 18.7, 27.5, 25.0, 22.7, 21.7, 22.7, 23.3, 25.0, 26.7, 18.7, 19.6, 23.9, 20.0, 17.2]

Umbral=22

#Funcion que Recibe una lista y retorna el promedio, maximo, minimo y valores debajo del umbral.
def main(lista):
    
    # La función mean() devuelve la media aritmética de los datos de una muestra o población. 
    # Esta media se calcula sumando todos los valores y después el resultado de la suma se divide entre el número de elementos.

    Temperatura_Promedio = round(stats.mean(Temperaturas1),2)

    # Fuente: https://python-para-impacientes.blogspot.com/2016/10/calculo-estadistico.html#:~:text=La%20funci%C3%B3n%20mean()%20devuelve,entre%20el%20n%C3%BAmero%20de%20elementos.
    
    
    Temperatura_Maxima = max(Temperaturas1)
    Temperatura_Minima = min(Temperaturas1)
    

    Temperatura_Umbral=[] #variable local dentro de la funcion main()

    for valor in lista:
        if valor < Umbral:
            Temperatura_Umbral.append(valor)

    return(Temperatura_Promedio, Temperatura_Maxima, Temperatura_Minima, Temperatura_Umbral)

#Funcion que imprime el promedio, maximo, minimo y valores debajo del umbral de una lista que se le de.
def imprimir(lista):
    print(f"La temperatura promedio es de {lista[0]}°C")
    print(f"La temperatura Maxima es de {lista[1]}°C y la Minima es de {lista[2]}°C")
    
    
    print(f"Las temperaturas por debajo del umbral (Total: {len(lista[3])}) son:")
    for x in range(len(lista[3])):
        print(F"_{lista[3][x]}°C")

#BUCLE PRINCIPAL
while True:

    Opcion = input( "Seleccione una lista de temperaturas a analizar: \n"
                    "1_Listado de Temperaturas 1 \n"
                    "2_Listado de Temperaturas 2 \n"
                    "3_Listado de Temperaturas 3 \n")

    Retorno = []#inicializo la lista en cero

    if Opcion == "1":
        Retorno = main(Temperaturas1)
        print("Lista 1:")
        imprimir(Retorno)
    elif Opcion == "2":
        Retorno = main(Temperaturas2)
        print("Lista 2:")
        imprimir(Retorno)
    elif Opcion == "3":
        Retorno = main(Temperaturas3)
        print("Lista 3:")
        imprimir(Retorno)
    else: 
        print("Ingrese un valor valido")

    

 
