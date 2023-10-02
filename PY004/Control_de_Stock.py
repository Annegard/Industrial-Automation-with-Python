#Control de stock:

# Verificar si los productos tienen cantidades inferiores al punto de reposicion y mostrar los productos con cantidades bajas.

productos_stock = {'producto1': 15, 'producto2': 7, 'producto3': 11, 'producto4': 5}

Umbral= 10

# Utilizar un bucle for para recorrer las claves y los valores del diccionario y una instruccion if para verificar si alguna cantidad 
# es inferior al punto de reposicion.

# Imprimir los productos con cantidades bajas y sus cantidades actuales,
# en un texto que sea amigable para el operario.

for clave, valor in productos_stock.items():
    if valor < Umbral:
        print(f"Del {clave} se posee un stock de {valor} unidades. {Umbral - valor} Unidades por debajo del punto de reposicion")

        # Nota:
        # PEP 498 introdujo un nuevo mecanismo de formato de cadenas conocido como interpolación de cadenas literales o más 
        # comúnmente como cadenas F (debido al carácter f inicial que precede al literal de cadena). La idea detrás de f-strings 
        # es simplificar la interpolación de cadenas. 
        # Para crear una cadena f, preceda la cadena con la letra "f". La cadena en sí se puede formatear de la misma manera que 
        # lo haría con str.format() . Las cadenas F proporcionan una manera concisa y conveniente de incrustar expresiones de 
        # Python dentro de cadenas literales para formatear. 

        # # Python3 program introducing f-string
        # val = 'Geeks'
        # print(f"{val}for{val} is a portal for {val}.")
        
        # name = 'Tushar'
        # age = 23
        # print(f"Hello, My name is {name} and I'm {age} years old.")

        #Fuente: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/