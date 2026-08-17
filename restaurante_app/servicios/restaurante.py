import os
os.system("cls")

from modelos.producto import Producto
from modelos.usuario import Usuario

class Restaurante:
    MENU_OPCIONES: Tuple[str, ...] = (
        "Registrar producto",
        "Buscar producto",
        "Actualizar producto",
        "Eliminar producto",
        "Listar productos",
        "Registrar usuario",
        "Listar usuarios",
        "Mostrar categorías",
        "Salir"
    )

    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
        self._acciones_menu: Dict[int, Callable[[], None]] = {
            1: self._registrar_producto_interactivo,
            2: self._buscar_producto_interactivo,
            3: self._actualizar_producto_interactivo,
            4: self._eliminar_producto_interactivo,
            5: self._listar_productos,
            6: self._registrar_usuario_interactivo,
            7: self._listar_usuarios,
            8: self._mostrar_categorias,
        }

    def _registrar_producto_interactivo(self) -> None:
        print("\n--- Registrar Producto ---")
        try:
            codigo = input("Código del producto: ").strip()
            if not codigo:
                print("Error: El código no puede estar vacío")
                return
            if self.buscar_producto(codigo):
                print("Error: Ya existe un producto con ese código")
                return

            nombre = input("Nombre del producto: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío")
                return

            categoria = input("Categoría del producto: ").strip()
            if not categoria:
                print("Error: La categoría no puede estar vacía")
                return

            precio_str = input("Precio del producto: ").strip()
            if not precio_str:
                print("Error: El precio no puede estar vacío")
                return
            precio = float(precio_str)
            if precio < 0:
                print("Error: El precio no puede ser negativo")
                return

            producto = Producto(codigo, nombre, categoria, precio)
            self.registrar_producto(producto)
            print(f"Producto {nombre} registrado")
        except ValueError:
            print("Error: Precio debe ser un número válido")
        except Exception as e:
            print(f"Error: {e}")

    def _buscar_producto_interactivo(self) -> None:
        print("\n--- Buscar Producto ---")
        codigo = input("Código del producto a buscar: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío")
            return
        producto = self.buscar_producto(codigo)
        if producto:
            print(f"Producto encontrado: {producto}")
        else:
            print("Producto no encontrado")

    def _actualizar_producto_interactivo(self) -> None:
        print("\n--- Actualizar Producto ---")
        codigo = input("Código del producto a actualizar: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío")
            return
        producto = self.buscar_producto(codigo)
        if not producto:
            print("Producto no encontrado")
            return

        print(f"Datos actuales: {producto}")
        print("Deje en blanco para mantener el valor actual")

        nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip()
        categoria = input(f"Nueva categoría ({producto.categoria}): ").strip()
        precio_str = input(f"Nuevo precio ({producto.precio:.2f}): ").strip()

        try:
            nuevo_nombre = nombre if nombre else None
            nueva_categoria = categoria if categoria else None
            nuevo_precio = float(precio_str) if precio_str else None

            if nuevo_precio is not None and nuevo_precio < 0:
                print("Error: El precio no puede ser negativo")
                return

            if self.actualizar_producto(codigo, nuevo_nombre, nueva_categoria, nuevo_precio):
                print("Producto actualizado")
            else:
                print("Error al actualizar el producto")
        except ValueError:
            print("Error: Precio debe ser un número válido")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def _eliminar_producto_interactivo(self) -> None:
        print("\n--- Eliminar Producto ---")
        codigo = input("Código del producto a eliminar: ").strip()
        if not codigo:
            print("Error: El código no puede estar vacío")
            return
        if self.eliminar_producto(codigo):
            print("Producto eliminado")
        else:
            print("Producto no encontrado")

    def _listar_productos(self) -> None:
        print("\n--- Lista de Productos ---")
        productos = self.listar_productos()
        if not productos:
            print("No hay productos registrados")
            return
        for i, producto in enumerate(productos, 1):
            print(f"{i}. {producto}")

    def _registrar_usuario_interactivo(self) -> None:
        print("\n--- Registrar Usuario ---")
        try:
            identificacion = input("Identificación del usuario: ").strip()
            if not identificacion:
                print("Error: La identificación no puede estar vacía")
                return
            if self.buscar_usuario(identificacion):
                print("Error: Ya existe un usuario con esa identificación")
                return

            nombre = input("Nombre del usuario: ").strip()
            if not nombre:
                print("Error: El nombre no puede estar vacío")
                return

            correo = input("Correo del usuario: ").strip()
            if not correo:
                print("Error: El correo no puede estar vacío")
                return

            usuario = Usuario(identificacion, nombre, correo)
            self.registrar_usuario(usuario)
            print(f"Usuario {nombre} registrado exitosamente")
        except Exception as e:
            print(f"Error inesperado: {e}")

    def _listar_usuarios(self) -> None:
        print("\n--- Lista de Usuarios ---")
        usuarios = self.listar_usuarios()
        if not usuarios:
            print("No hay usuarios registrados")
            return
        for i, usuario in enumerate(usuarios, 1):
            print(f"{i}. {usuario}")

    def _mostrar_categorias(self) -> None:
        print("\n--- Categorías de Productos ---")
        categorias = self.obtener_categorias_unicas()
        if not categorias:
            print("No hay categorías registradas")
            return
        print("Categorías disponibles:")
        for categoria in sorted(categorias):
            print(f"  • {categoria}")

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(self, codigo: str, nombre: Optional[str] = None,
                           categoria: Optional[str] = None, precio: Optional[float] = None) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False
        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        for i, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                del self._productos[i]
                return True
        return False

    def listar_productos(self) -> List[Producto]:
        return self._productos.copy()

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def listar_usuarios(self) -> List[Usuario]:
        return self._usuarios.copy()

    def obtener_categorias_unicas(self) -> Set[str]:
        categorias: Set[str] = set()
        for producto in self._productos:
            categorias.add(producto.categoria)
        return categorias

    def get_opciones_menu(self) -> Tuple[str, ...]:
        return self.MENU_OPCIONES

    def ejecutar_opcion(self, opcion: int) -> bool:
        if opcion == 9:
            return False
        accion = self._acciones_menu.get(opcion)
        if accion:
            accion()
            return True
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")
        return True