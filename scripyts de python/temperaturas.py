# Verificar si las temperaturas registradas superan el umbral predefinido
# y mostrar las temperaturas anormales encontradas
# Umbral: 30 grados celsius
# Utilizar un bucle for para recorrer la lista de temperaturas y una instruccion if 
# para verificar si cada temperatura supera el umbral.
# Crear una lista llamada temperaturas_anormales para almacenar las temperaturas que 
# superen el umbral.
# Al finalizar el bucle, imprimir las temperaturas anormales encontradas.

temperaturas = [28, 29, 31, 27, 33, 29, 30, 32, 28]
temperaturas_anormales = []

for temp in temperaturas:
    if temp > 30:
        temperaturas_anormales.append(temp)

print("Temperaturas: ")
print(temperaturas_anormales)