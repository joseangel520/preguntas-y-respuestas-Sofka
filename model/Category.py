''' 
    Clase encargada de gestionar la categoria del juego
    La clase cuenta con
  * Dos atributos privados, encargados de gestionar el nivel y los puntos
  * Un constructor encargado de iniciar el atributo del nivel
  * Un metodo encargado de retornar el nivel
  * Un metodo encargado de retornar los puntos
  * Un metodo encargador de incrementar los puntos del jugador
  * Un metodo encargado de validar los puntos requeridos para aumentar el nivel
  * Un metodo encargado de validar si tiene los puntos requeridos para ganar o retornara los puntos 
    obtenidos durante el juego
'''
class Category:
    __level
    __points

    # Contructorde la clase
    def __init__(self):
        self.__level = 1

    # Metodo encargado de retornar el nivel
    def getLevel(self):
        return self.__level

    # Metodo encargado de retornar los puntos
    def getPoints(self):
        return self.__points

    # Metodo encargado de incrementar los puntos
    def increasePoint(self):
        self.__points = self.__points + 5
        return self.__points

    # Metodo encargado de validar los puntos requeridos para aumentar el nivel
    def levelUp(self):
        if self.__points == 25: 
            self.__level = 2
            return self.__level
        if self.__points == 50:
            self.__level = 3
            return self.__level
        if self.__points == 75:
            self.__level = 4
            return self.__level
        else:
            self.__level = 5 
            return self.__level

    # Metodo encargado de validar los puntos requeridos para Ganar
    def Winner(self):
        if self.__level == 150:
            return "Felicitaciones Eres el Gran ganador de un abrazo y un gracias"
        return self.__points
