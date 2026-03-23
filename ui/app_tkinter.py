import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante


class AppVisitas(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Sistema de Registro de Visitantes - Teocac S.A.")
        self.geometry("600x450")

        # Variables de control
        self.var_cedula = tk.StringVar()
        self.var_nombre = tk.StringVar()
        self.var_motivo = tk.StringVar()

        self._crear_interfaz()
        self._actualizar_tabla()

    def _crear_interfaz(self):
        # Formulario
        frame_form = tk.LabelFrame(self, text="Datos del Visitante", padx=10, pady=10)
        frame_form.pack(fill="x", padx=20, pady=10)

        tk.Label(frame_form, text="Cédula:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_cedula).grid(row=0, column=1, pady=5)

        tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_nombre, width=30).grid(row=1, column=1, pady=5)

        tk.Label(frame_form, text="Motivo:").grid(row=2, column=0, sticky="w")
        tk.Entry(frame_form, textvariable=self.var_motivo, width=30).grid(row=2, column=1, pady=5)

        # Botones
        frame_btns = tk.Frame(self)
        frame_btns.pack(pady=10)

        tk.Button(frame_btns, text="Registrar", command=self._registrar, bg="green", fg="white").pack(side="left",
                                                                                                      padx=5)
        tk.Button(frame_btns, text="Eliminar Seleccionado", command=self._eliminar, bg="red", fg="white").pack(
            side="left", padx=5)
        tk.Button(frame_btns, text="Limpiar Campos", command=self._limpiar_campos).pack(side="left", padx=5)

        # Tabla (Treeview)
        self.tabla = ttk.Treeview(self, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tabla.heading("Cedula", text="Cédula")
        self.tabla.heading("Nombre", text="Nombre Completo")
        self.tabla.heading("Motivo", text="Motivo de Visita")
        self.tabla.pack(fill="both", expand=True, padx=20, pady=10)

    def _registrar(self):
        c, n, m = self.var_cedula.get(), self.var_nombre.get(), self.var_motivo.get()
        if not (c and n and m):
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        nuevo = Visitante(c, n, m)
        exito, msg = self.servicio.registrar_visitante(nuevo)

        if exito:
            messagebox.showinfo("Éxito", msg)
            self._limpiar_campos()
            self._actualizar_tabla()
        else:
            messagebox.showerror("Error", msg)

    def _eliminar(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un registro para eliminar")
            return

        item = self.tabla.item(seleccion)
        cedula = item['values'][0]

        if self.servicio.eliminar_visitante(str(cedula)):
            messagebox.showinfo("Eliminado", "Visitante eliminado correctamente")
            self._actualizar_tabla()

    def _limpiar_campos(self):
        self.var_cedula.set("")
        self.var_nombre.set("")
        self.var_motivo.set("")

    def _actualizar_tabla(self):
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        # Cargar datos desde el servicio
        for v in self.servicio.obtener_todos():
            self.tabla.insert("", "end", values=(v.cedula, v.nombre, v.motivo))