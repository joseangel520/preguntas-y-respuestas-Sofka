from tkinter import ttk
from controllers.Controller import Controller
# from model.NumberQuestion import NumberQuestion
import tkinter as tk

class View(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.title = ('Preguntas y Respuestas')
        self.answer = tk.StringVar()

        # Creando widgets
        # Label donde se mostrara la preguntas
        self.preguntas = ttk.Label(self, text='Pregunta')

        # Radio buttons respuestas
        self.radioA = ttk.Radiobutton(self, text='A', value='A', variable=self.answer, command=self.selected)
        self.radioA.config(state = 'disabled')
        
        self.radioB = ttk.Radiobutton(self, text='B', value='B', variable=self.answer, command=self.selected)
        self.radioB.config(state = 'disabled')
        
        self.radioC = ttk.Radiobutton(self, text='C', value='C', variable=self.answer, command=self.selected)
        self.radioC.config(state = 'disabled')
        
        self.radioD = ttk.Radiobutton(self, text='D', value='D', variable=self.answer, command=self.selected)
        self.radioD.config(state = 'disabled')


        # Buttones para iniciar el Juego, Terminar, Salir y Siguiente
        self.btnStarGame = ttk.Button(self, text="Iniciar Juego")
        self.btnStarGame['command'] = self.startGame
        self.btnEndGame = ttk.Button(self, text="Terminar Juego")
        self.btnEndGame.state(['disabled'])
        self.btnEndGame['command'] = self.endGame
        self.btnExit = ttk.Button(self, text="Salir Juego")
        self.btnExit['command'] = self.exitGame
        self.btnNext = ttk.Button(self, text = "Siguente Pregunta")
        self.btnNext.state(['disabled'])
        self.btnNext['command'] = self.next
        
        # Agregando los widgets a la ventana
        # Label preguntas
        self.preguntas.grid(row = 1, column = 0)

        # Radio buttons respuestas
        self.radioB.grid(row = 3, column = 0)
        self.radioC.grid(row = 4, column = 0)
        self.radioA.grid(row = 2, column = 0)
        self.radioD.grid(row = 5, column = 0)

        # Bottons funcionalidades de inicio, terminar, salir y siguiente
        self.btnStarGame.grid(row = 2, column = 2)
        self.btnEndGame.grid(row = 3, column = 2)
        self.btnExit.grid(row = 4, column = 2)
        self.btnNext.grid(row = 5, column = 2)
    
    def setController(self, controller):
        self.controller = controller

    def startGame(self):
        self.radioA.config(state = 'enable')
        self.radioB.config(state = 'enable')
        self.radioC.config(state = 'enable')
        self.radioD.config(state = 'enable')
        self.btnNext.state(['!disabled'])
        self.btnEndGame.state(['!disabled'])
        self.controller.startGameState()

    def endGame(self):
        print("Termino el Juego")
    
    def exitGame(self):
        self.quit()

    def next(self):
        print("Siguiente Pregunta")

    # Metodo encargado de verificar la opcion que selecciono el usuario
    def selected(self):
        if self.answer.get() == "A":
            print("Selecciono A")
        elif self.answer.get() == 'B':
            print("Selecciono B")
        elif self.answer.get() == 'C':
            print("Selecciono C")
        else:
            print("Selecciono D")
