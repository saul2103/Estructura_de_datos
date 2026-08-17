import os
os.system("cls")


class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) - ${self.precio:.2f}"

    def __repr__(self) -> str:
        return f"Producto(codigo='{self.codigo}', nombre='{self.nombre}', categoria='{self.categoria}', precio={self.precio})"