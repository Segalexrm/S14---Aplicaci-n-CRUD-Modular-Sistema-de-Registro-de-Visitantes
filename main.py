from servicios.visita_servicio import VisitaServicio
from ui.app_tkinter import AppVisitas


def main():
    # 1. Instanciar el servicio (Cerebro)
    servicio = VisitaServicio()

    # 2. Inyectar el servicio en la UI
    app = AppVisitas(servicio)

    # 3. Ejecutar
    app.mainloop()


if __name__ == "__main__":
    main()