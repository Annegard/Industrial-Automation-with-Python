# Tanque:

# Crear una clase base llamada Tanque con atributos de instancias como diámetro, altura y nivel máximo.

# Además, debe tener otras variables como nivelActual, caudalConsumo y caudalIngreso. 

# Definir métodos para el control del tanque: llenar, vaciar, medirLitrosCrea una clase derivada llamada 
# TanqueConValvulas que herede de Tanque e incluya atributos adicionales como el número de válvulas, su
# estado (abierta/cerrada) y su función (llenado/vaciado)
# Define un método vacío llamado abrir_valvula() que represente la 
# acción de abrir una válvula en el tanque con válvulas.

class Servo(Motor):   
    def __init__(self, potencia, voltaje, fabricante):       
        super().__init__(potencia, voltaje, fabricante)       
        self.posicion = 0
