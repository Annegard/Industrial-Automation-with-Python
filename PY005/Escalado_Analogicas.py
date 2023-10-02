# Escalado de Analogicas:

# Escribe una funcion llamada "escalar_valores" que reciba un valor analogico como argumento y 
# lo escale literalmente segun un rango de entrada y un rango de salida especificos.

# El objetivo es transformar el valor analogico desde el rango de entrada al de salida.

# valor_analogico: El valor analogico a escalar.
# minimo_ing: El valor minimo del rango de entrada. Default = 0
# maximo_ing: El valor maximo del rango de entrada. Default = 32767 [2^15 (el bit restante es para el signo)]
# minimo: El valor minimo del rango de salida. Default = 0.0
# maximo: El valor maximo del rango de salida. Default = 100.0

def escalar_valores(valor_analogico, min_ing=0, max_ing=32767, min=0, max=100):

    #creo que una variable local a la funcion
    valor_salida = ((int(valor_analogico)/(max_ing-min_ing))*(max-min))+min

    return(valor_salida)

Val_Max_PT1000=1000 #Valor maximo que puede medir una PT1000 en Grados
Val_Min_PT1000=-200 #Valor minimo que puede medir una PT1000 en Grados
Val_Max_Input =32767 #Valor maximo que puede llegar a recibir un ADC de 15 bits
Val_Min_Input =0 #Valor minimo que puede llegar a recibir una ADC de 15 bits

while True:
    valor_analogico = input("Ingrese el valor analogico: ")
    Retorno_de_funcion = escalar_valores(valor_analogico, Val_Min_Input,Val_Max_Input,Val_Min_PT1000,Val_Max_PT1000)

    print(f"La temperatura es de: {Retorno_de_funcion} °C")

    print(Retorno_de_funcion)

