import sqlite3
from tkinter import messagebox

class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
    
    def cerrar(self):
        try:
            self.conexion.commit()
            self.conexion.close()
        except:
            messagebox.showerror('Conexion BD', 'No se ha podido conectar a la Base de Datos')