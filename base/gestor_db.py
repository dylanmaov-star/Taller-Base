import mysql.connector

class GestorBaseDatos:
    def __init__(self, host="localhost", user="root", password="", database="escuela"):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database
        }

    def conectar(self):
        try:
            conexion = mysql.connector.connect(**self.config)
            if conexion.is_connected():
                return conexion
        except:
            return None