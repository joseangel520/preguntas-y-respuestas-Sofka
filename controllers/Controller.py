from model.Question import Question
# from model.Answer import Answer 
# from view.View import Views

class Controller:

    def __init__(self, question, vista):
        self.question = question
        self.view = vista
    

    def startGameState(self):
        print("Inicio el juego")
    