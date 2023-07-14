from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()

    sql = '''
            CREATE TABLE peliculas(
                id_pelicula INTEGER,
                nombre VARCHAR(100),
                duracion VARCHAR(10),
                genero VARCHAR(100),
                PRIMARY KEY(id_pelicula AUTOINCREMENT) 
            )
          '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('¡Crear Tabla!', 'Se ha creado exitosamente la tabla en la Base de Datos')
    except:
        messagebox.showwarning('¡Crear Tabla!', 'La tabla ya existe en la Base de Datos')

def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo('¡Borrar Tabla!', 'Se ha borrado exitosamente la tabla en la Base de Datos')
    except:
        messagebox.showerror('¡Borrar Tabla!', 'La tabla peliculas no existe en la Base de Datos')

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
    
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

    def guardar(pelicula):
        conexion = ConexionDB()
        
        sql = f"""INSERT INTO peliculas (nombre, duracion, genero)
            VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""
        
        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo('Guardar Registro', 'Se ha guardado el registro exitosamente')
        except:
            messagebox.showerror('Error', 'No está creada la tabla en la Base de Datos')
    
    def listar():
        conexion = ConexionDB()

        lista_peliculas = []
        sql = 'SELECT * FROM peliculas'

        try:
            conexion.cursor.execute(sql)
            lista_peliculas = conexion.cursor.fetchall()
            conexion.cerrar()
        except:
            messagebox.showwarning('¡Advertencia', 'La tabla no existe en la base de datos')
        
        return lista_peliculas

    def editar(pelicula, id_pelicula):
        conexion = ConexionDB()

        sql = f"""UPDATE peliculas
                SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}', genero = '{pelicula.genero}'
                WHERE id_pelicula = '{id_pelicula}'"""

        try:
            conexion.cursor.execute(sql)
            conexion.cerrar()
            messagebox.showinfo('Actualización', 'Se ha actualizado exitosamente')
        except:
            messagebox.showwarning('Error', 'No se ha podido actualizar el registro')

    def eliminar(id_pelicula):
        conexion = ConexionDB()
        sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

        try:
            conexion.cursor.execute(sql)
            messagebox.askyesno('Borrar Registro', '¿Está seguro de Borrar el Registro?')
            conexion.cerrar()
        except:
            messagebox.showerror('Error', 'No se ha podido eliminar el Registro')