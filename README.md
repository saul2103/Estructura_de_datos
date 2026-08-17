# Sistema de Restaurante Recetas de mi Sierra
**Estudiante:** Bryan Saul Iza Llano

## Descripción del Sistema

Sistema de administración básica para restaurantes que permite gestionar productos y usuarios registrados. Desarrollado en Python con arquitectura modular, aplicando las principales estructuras de datos del lenguaje para resolver necesidades específicas del negocio.

## Estructura del Proyecto
```
restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py # Clase Producto (código, nombre, categoría, precio)
│ └── usuario.py # Clase Usuario (identificación, nombre, correo)
├── servicios/
│ ├── init.py
│ └── restaurante.py # Clase Restaurante (lógica de negocio y colecciones)
├── main.py # Punto de entrada y menú interactivo
└── README.md # Documentación del proyecto
```
## Responsabilidad de Componentes

### modelos/
Contiene las clases que representan las entidades del sistema. Son estructuras simples sin lógica de negocio, solo definen atributos y métodos básicos como `__str__`.

- **producto.py**: Define la clase `Producto` con atributos: código, nombre, categoría y precio.
- **usuario.py**: Define la clase `Usuario` con atributos: identificación, nombre y correo.

### servicios/
Contiene la lógica de negocio y administración de colecciones.

- **restaurante.py**: Clase `Restaurante` que:
  - Mantiene colecciones de productos y usuarios
  - Implementa operaciones CRUD
  - Valida reglas de negocio (códigos únicos, precios válidos)
  - Coordina el menú y las acciones del sistema

### main.py
Punto de entrada del programa. Coordina:
- Visualización del menú interactivo
- Captura de datos del usuario mediante `input()`
- Invocación de métodos del servicio `Restaurante`
- Manejo de excepciones y validaciones básicas

## Aplicación de Estructuras de Datos

### Lista (`list`)
**Ubicación**: `servicios/restaurante.py`

**Propósito**: Administrar colecciones dinámicas de objetos.

- `_productos: List[Producto]` - Almacena todos los productos registrados
- `_usuarios: List[Usuario]` - Almacena todos los usuarios registrados

**Justificación**: Las listas permiten agregar, eliminar, buscar y recorrer elementos de forma eficiente. Son ideales para colecciones que cambian dinámicamente durante la ejecución del programa.

### Tupla (`tuple`)
**Ubicación**: `servicios/restaurante.py`

**Propósito**: Representar información estable que no debe modificarse.

- `MENU_OPCIONES: Tuple[str, ...]` - Opciones fijas del menú principal

**Justificación**: Las tuplas garantizan inmutabilidad, evitando modificaciones accidentales de las opciones del menú durante la ejecución. Son más eficientes en memoria que las listas para datos estáticos.

### Diccionario (`dict`)
**Ubicación**: `servicios/restaurante.py`

**Propósito**: Establecer relaciones clave → valor para acceso rápido.


**Justificación**: Los diccionarios ofrecen acceso O(1) a las funciones según la opción seleccionada, eliminando la necesidad de múltiples condicionales `if-elif`. Mejoran la legibilidad y mantenibilidad del código.

### Conjunto (`set`)
**Ubicación**: `servicios/restaurante.py` - Método `obtener_categorias_unicas()`

**Propósito**: Obtener y mostrar valores sin duplicados.

- `categorias: Set[str]` - Categorías únicas de todos los productos

**Justificación**: Los conjuntos eliminan automáticamente duplicados, lo que permite obtener fácilmente todas las categorías existentes sin necesidad de implementar lógica adicional de verificación.

## Instrucciones para Ejecutar

- Python 3.6 o superior
- Terminal o consola