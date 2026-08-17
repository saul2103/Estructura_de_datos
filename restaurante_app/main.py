import os
os.system("cls")

from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.usuario import Usuario

def mostrar_menu(opciones: tuple) -> None:
    print("\n" + "=" * 40)
    print("        RECETAS DE MI SIERRA")
    print("=" * 40)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
    print("=" * 40)

def main() -> None:
    restaurante = Restaurante()
    opciones = restaurante.get_opciones_menu()

    while True:
        mostrar_menu(opciones)
        try:
            opcion_str = input("Seleccione una opción: ").strip()
            if not opcion_str:
                print("Por favor, ingrese un número")
                continue
            opcion = int(opcion_str)
            if not restaurante.ejecutar_opcion(opcion):
                print("\n¡Gracias por usar el Sistema del Restaurante!")
                break
            input("\nPresione Enter para continuar...")
        except ValueError:
            print("Error: Por favor, ingrese un número válido")
        except KeyboardInterrupt:
            print("\n\n¡Gracias por usar el Sistema del Restaurante!")
            break
        except Exception as e:
            print(f"Error : {e}")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()