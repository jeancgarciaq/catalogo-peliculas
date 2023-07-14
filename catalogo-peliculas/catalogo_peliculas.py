import tkinter as tk
from client.gui_app import Frame, barra_menu 

def main():
    root = tk.Tk()
    root.title('Catálogo de Películas')
    root.iconbitmap('img/favicon.ico')
    # resizable se usa para evitar que se amplie la ventana root.resizable(0,0) 0 = False, 1 = True
    barra_menu(root)
    app = Frame(root=root)
    app.mainloop()

if __name__ == '__main__':
    main()