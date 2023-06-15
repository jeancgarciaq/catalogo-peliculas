from tkinter import *
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc, ttk
from typing import Any
from typing_extensions import Literal

class Frame(Frame):
    def __init__(self, root = None):
        #Aqui hay que colocar constructor padre
        self.root = root
        self.grid()
        self.config(width= 480, height= 320)
        # Modificar el icono self.iconbitmap('img/nombredelarchivo')
        # Impedir que se modifique el tamaño de la ventana self.resizable(0,0) equivale a false, false