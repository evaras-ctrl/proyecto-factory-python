from .base import Notificacion


class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[Email] {mensaje}")


class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[SMS] {mensaje}")


class NotificacionPush(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"[Push] {mensaje}")