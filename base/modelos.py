class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"ID: {self.id} | Producto: {self.nombre} | Precio: ${self.precio}"

class Cliente:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def mostrar_info(self):
        return f"Cliente: {self.nombre} | Contacto: {self.correo}"