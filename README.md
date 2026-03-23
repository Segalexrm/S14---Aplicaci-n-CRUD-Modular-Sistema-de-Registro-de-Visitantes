# 📝 Sistema de Registro de Visitantes (CRUD Modular)

Este proyecto es una aplicación de escritorio desarrollada en **Python** utilizando la librería **Tkinter**. El sistema permite gestionar el flujo de visitantes a una oficina mediante una arquitectura modular por capas, garantizando la separación de la lógica de negocio y la interfaz de usuario.

## Objetivo del Proyecto
Demostrar el dominio de la **Programación Orientada a Objetos (POO)** y la implementación de una arquitectura limpia, aplicando conceptos como:
* **Encapsulamiento:** Gestión interna de datos en la capa de servicios.
* **Inyección de Dependencias:** La interfaz gráfica recibe el servicio como parámetro.
* **Modularidad:** Separación estricta en carpetas (Modelos, Servicios, UI, Main).

---

## Estructura del Repositorio
Siguiendo los requerimientos académicos de la **Universidad Estatal Amazónica**, el proyecto se organiza de la siguiente manera:

```text
tarea_poo_visitas/
│
├── main.py                # Punto de entrada de la aplicación.
├── modelos/
│   └── visitante.py       # Definición de la clase Visitante (Atributos).
├── servicios/
│   └── visita_servicio.py # Lógica de negocio y operaciones CRUD.
└── ui/
    └── app_tkinter.py     # Capa visual e interacción con el usuario.
```

---

## Funcionalidades
*  **Registro:** Captura de Cédula, Nombre y Motivo de visita con validaciones.
*  **Visualización:** Tabla dinámica (`Treeview`) para listar registros en tiempo real.
*  **Eliminación:** Borrado de registros seleccionados directamente desde la tabla.
*  **Limpieza:** Función para resetear los campos del formulario.
*  **Notificaciones:** Mensajes de confirmación y advertencia mediante `messagebox`.

---

##  Requisitos e Instalación

1.  **Lenguaje:** Python 3.x
2.  **Librerías:** Únicamente la librería estándar `tkinter` (incluida en Python).
3.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Segalexrm/S14---Aplicaci-n-CRUD-Modular-Sistema-de-Registro-de-Visitantes.git
    ```

##  Ejecución
Para iniciar el sistema, ejecuta el siguiente comando desde la terminal en la carpeta raíz del proyecto:

```bash
python main.py
```