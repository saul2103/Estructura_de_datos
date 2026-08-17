import os
os.system("cls")


class Usuario:
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def __str__(self) -> str:
        return f"{self.identificacion} - {self.nombre} ({self.correo})"

    def __repr__(self) -> str:
        return f"Usuario(identificacion='{self.identificacion}', nombre='{self.nombre}', correo='{self.correo}')"