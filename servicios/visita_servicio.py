class VisitaServicio:
    def __init__(self):
        # Persistencia en memoria
        self._visitantes = []

    def registrar_visitante(self, visitante):
        # Validar que no exista la cédula
        for v in self._visitantes:
            if v.cedula == visitante.cedula:
                return False, "La cédula ya está registrada."

        self._visitantes.append(visitante)
        return True, "Registro exitoso."

    def obtener_todos(self):
        return self._visitantes

    def eliminar_visitante(self, cedula):
        for v in self._visitantes:
            if v.cedula == cedula:
                self._visitantes.remove(v)
                return True
        return False