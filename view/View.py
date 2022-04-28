from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.title = ('Datos del Usuario')
        
        # Creando widgets
        # Label Informacion Jugador
        self.playerName = ttk.Label(self, text="Nombre Jugador: ")
        self.surnamePlayer = ttk.Label(self, text="Apellido Jugador: ")
        self.emailPlayer = ttk.Label(self, text="Email Jugador: ")
        
        
        
        self.playerName.grid(row=1, column=0)
        self.surnamePlayer.grid(row=2, column=0)
        self.emailPlayer.grid(row=3, column=0)





