''' 
  Clase encargada donde se crean las respuestas de las preguntas
  La clase cuenta con
  * Una matriz encargada de tener las respuestas
  * Un metodo de traer la respuesta
  * Un metodo encargado de relizar la validacion respectiva de la pregunta seleccionada por el
  * usuario con la que se encuentra almacenada en la matriz.
'''
class Answer:
    # Matriz en cargada de tener todas las respuestas de las preguntas
    # Esta se encuentra protegida por el modificador de acceso __
    __answers = [[]]

    # Funcion encargada de obtener la respuesta de la matriz
    def getAnswer(self, numberCuestion):
        return self.__answers[numberCuestion][0]
    
    # Funcion encargada de veluar la respuesta seleccionada por el usuario
    # y con la que se encuentra en el array
    def evaluatequestion(self, selectQuestion, numberCuestion):
        if self.__answers[numberCuestion][1] == self.selectQuestion:
            return True
        else:
            return False
        return False