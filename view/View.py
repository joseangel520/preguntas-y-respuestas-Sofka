from tkinter import ttk
import tkinter as tk


class View(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)

        self.title = ('Datos del Usuario')
        self.answer = tk.StringVar()

        # Creando widgets
        # Label donde se mostrara la preguntas
        self.preguntas = ttk.Label(self, text='Pregunta')
        self.preguntas.grid(row=1, column=0)

        # Radio buttons respuestas
        self.radioA = ttk.Radiobutton(self, text='A', value='A', variable=self.answer, command=self.selected)
        self.radioB = ttk.Radiobutton(self, text='B', value='B', variable=self.answer, command=self.selected)
        self.radioC = ttk.Radiobutton(self, text='C', value='C', variable=self.answer, command=self.selected)
        self.radioD = ttk.Radiobutton(self, text='D', value='D', variable=self.answer, command=self.selected)

        self.radioA.grid(row=2, column=0)
        self.radioB.grid(row=3, column=0)
        self.radioC.grid(row=4, column=0)
        self.radioD.grid(row=5, column=0)

    def selected(self):
        if self.answer.get() == "A":
            print("Selecciono A")
        elif self.answer.get() == 'B':
            print("Selecciono B")
        elif self.answer.get() == 'C':
            print("Selecciono C")
        else:
            print("Selecciono D")
