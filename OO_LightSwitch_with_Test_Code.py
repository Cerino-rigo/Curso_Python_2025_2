# OO_LightSwitch

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # turn the switch on 
         self.switchIsOn = True

    def turnOff(self):
        # turn the switch off
         self.switchIsOn = False

    def show(self):  # added for testing
        print(self.switchIsOn)
    
# Main code
oLightSwitch = LightSwitch()  # create a LightSwitch object

#  Calls to methods
oLightSwitch.show() # call the show method of oLightSwitch
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOff() # call the turnOff method of oLightSwitch
oLightSwitch.show()
oLightSwitch.turnOn() # call the turnOn method of oLightSwitch
oLightSwitch.show()

'''
Se crea una clase LightSwitch que encapsula:
Estado: self.switchIsOn.
Comportamiento: turnOn, turnOff, show.
Crear una instancia (objeto) de la clase: oLightSwitch = LightSwitch().
El estado pertenece al objeto; no hay variables globales.
Ventajas visibles:
Múltiples interruptores: puedes crear varias instancias LightSwitch() sin interferencias entre ellas.
Organización: estado y comportamiento están agrupados.
Interfaz clara: se interactúa con métodos (turnOn, turnOff, show) y no con variables internas.
'''