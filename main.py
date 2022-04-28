import tkinter as tk
from model.Question import Question
from view.View import View
from controllers.Controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()
     
        self.geometry('300x50')

        # Creando el Modelo
        question = Question()

        # Inicialiando la vista.
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # Creando el Controlador
        controller = Controller(question, view)

        # Configurando el controlador en la vista
        # view.setController(controller)


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()