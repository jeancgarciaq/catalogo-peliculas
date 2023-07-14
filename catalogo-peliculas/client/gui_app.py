import tkinter as tk
from tkinter import ttk, messagebox
from model.pelicula_dao import crear_tabla, borrar_tabla
from model.pelicula_dao import Pelicula

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, bg='light gray', fg='black', activebackground='sky blue', tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB', command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB', command=borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    consulta = tk.Menu(barra_menu, bg='light gray', fg='black', activebackground='sky blue', tearoff=0)
    barra_menu.add_cascade(label='Consulta', menu=consulta)
    
    configuracion = tk.Menu(barra_menu, bg='light gray', fg='black', activebackground='sky blue', tearoff=0)
    barra_menu.add_cascade(label='Configuración', menu=configuracion)
    
    ayuda = tk.Menu(barra_menu, bg='light gray', fg='black', activebackground='sky blue', tearoff=0)
    barra_menu.add_cascade(label='Ayuda', menu=ayuda)

class Frame(tk.Frame):
    def __init__(self, root = None):
        #Aqui hay que colocar constructor padre
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        self.id_pelicula = None

        self.campos_peliculas()
        self.deshabilitar_campos()
        self.tabla_peliculas()
    
    def campos_peliculas(self):
        #Labels de campos
        self.label_nombre = tk.Label(self, text='Nombre: ', font='Arial 12 bold', padx=10, pady=10)
        self.label_nombre.grid(row=0, column=0)

        self.label_duracion = tk.Label(self, text='Duración: ', font='Arial 12 bold', padx=10, pady=10)
        self.label_duracion.grid(row=1, column=0)

        self.label_genero = tk.Label(self, text='Género: ', font='Arial 12 bold', padx=10, pady=10)
        self.label_genero.grid(row=2, column=0)
        
        #Entradas de campos
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, width=50, font='Arial 12', textvariable=self.mi_nombre)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, width=50, font='Arial 12', textvariable=self.mi_duracion)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, width=50, font='Arial 12', textvariable=self.mi_genero)
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #botones
        self.boton_nuevo = tk.Button(self, text='Nuevo', bg='#158645', width=20, font='Arial 12 bold', fg='#dad5d6', cursor='hand2', activebackground='#35bd6f',
                                     command=self.habilitar_campos)
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar', bg='#1658a2', width=20, font='Arial 12 bold', fg='#dad5d6', cursor='hand2', activebackground='#3586df', 
                                       command=self.guardar_datos)
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar', bg='#bd152e', width=20, font='Arial 12 bold', fg='#dad5d6', cursor='hand2', activebackground='#e15370',
                                        command=self.deshabilitar_campos)
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
    
    def habilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.configure(state='normal')
        self.entry_duracion.configure(state='normal')
        self.entry_genero.configure(state='normal')

        self.boton_guardar.configure(state='normal')
        self.boton_cancelar.configure(state='normal')

    def deshabilitar_campos(self):
        self.id_pelicula = None
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        self.entry_nombre.configure(state='disabled')
        self.entry_duracion.configure(state='disabled')
        self.entry_genero.configure(state='disabled')

        self.boton_guardar.configure(state='disabled')
        self.boton_cancelar.configure(state='disabled')
    
    def guardar_datos(self):
        pelicula = Pelicula(self.mi_nombre.get(), self.mi_duracion.get(), self.mi_genero.get())
        
        if self.id_pelicula == None:
            pelicula.guardar()
        else:
            pelicula.editar(self.id_pelicula)
        
        self.tabla_peliculas()
        self.deshabilitar_campos()
        
    def tabla_peliculas(self):
        #Importamos la lista de la BD
        self.lista_peliculas = Pelicula.listar()
        self.lista_peliculas.reverse()

        #Creamos la tabla y sus encabezados
        self.tabla = ttk.Treeview(self, column = ('Nombre', 'Duración', 'Género'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky='nse')

        #Scrollbar para > 10 registros
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        #iterar sobre los datos recuperados
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1], p[2], p[3]))
        
        #botones
        self.boton_editar = tk.Button(self, text='Editar', bg='#158645', width=20, font='Arial 12 bold', fg='#dad5d6', cursor='hand2', activebackground='#35bd6f', command=self.editar_datos)
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        self.boton_eliminar = tk.Button(self, text='Eliminar', bg='#bd152e', width=20, font='Arial 12 bold', fg='#dad5d6', cursor='hand2', activebackground='#e15370', command=self.eliminar_datos)
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)
    
    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')

    def eliminar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            Pelicula.eliminar(self.id_pelicula)
            self.tabla_peliculas()
            self.id_pelicula = None
        except:
            messagebox.showerror('Error', 'No ha seleccionado ningún registro')