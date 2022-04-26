# Clase esta creada para poder gestionar manera clara, las preguntas
# Y como se podran enviar
class Question:
    __preguntas = [];

    # Metodo encargado de buscar la pregunta, recibiendo un numero 
    # Para poder compararlo
    def getPregunta(self, numero):
        return self.__preguntas[numero];