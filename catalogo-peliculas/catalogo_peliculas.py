from tkinter import *
from tkinter import ttk
from client.gui_app import Frame

def main():
    root = Tk()
    root.title('Catálogo de Películas')
    # Modificar el icono root.iconbitmap('img/nombredelarchivo')
    # Impedir que se modifique el tamaño de la ventana root.resizable(0,0) equivale a false, false
    
app = Frame(root = root)

if __name__ == '__main__':
    main()