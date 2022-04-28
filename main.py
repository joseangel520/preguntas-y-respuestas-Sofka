import tkinter as tk
# import view.View
from view.View import View


class App(tk.Tk):
    def __init__(self):
        super().__init__()

     
        self.geometry('300x50')

        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)


def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()