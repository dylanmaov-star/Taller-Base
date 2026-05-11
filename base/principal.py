from gestor_db import GestorBaseDatos
from modelos import Producto, Cliente

class Aplicacion:
    def __init__(self):
        self.db = GestorBaseDatos()
        
    def iniciar(self):
        print("--- SISTEMA DE GESTIÓN ---")
        conexion = self.db.conectar()
        
        if conexion:
            print("Conexión exitosa.\n")
            
            p1 = Producto(1, "Laptop", 1500)
            c1 = Cliente(101, "Edward", "edward@example.com")
            
            print("Resultados:")
            print("-" * 30)
            print(p1.mostrar_info())
            print(c1.mostrar_info())
            print("-" * 30)
            
            conexion.close()
        else:
            print("Error al conectar.")

if __name__ == "__main__":
    app = Aplicacion()
    app.iniciar()