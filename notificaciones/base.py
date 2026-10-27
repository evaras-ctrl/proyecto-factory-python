from abc import ABC, abstractmethod


class Notificacion(ABC):
    """Clase base (interfaz) para todos los tipos de notificación."""

    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass