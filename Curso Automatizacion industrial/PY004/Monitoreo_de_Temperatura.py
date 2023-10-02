# Monitoreo de Temperatura: 

# Verificar si las temperaturas registradas superan un umbral predefinido y mostrar las temperaturas anormales encontradas.

temperaturas = [28, 29, 31, 27, 33, 29, 30, 31, 32, 28]#grados Celsius

Umbral = 30 #grados Celsius

# Utilizar un bucle for para recorrer la lista de temperaturas y una instrucción if para verificar si cada temperatura supera el umbral.
# Crear una lista llamada temperaturas_anormales para almacenar las temperaturas que superen el umbral. 
# Al finalizar el bucle, imprimir las temperaturas anormales encontradas. 

temperaturas_anormales=[]

for valor in temperaturas:
    if valor > Umbral:
        temperaturas_anormales.append(valor)

print(temperaturas_anormales)