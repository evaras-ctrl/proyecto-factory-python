class Notificacion:
    def enviar(self, mensaje):
        raise NotImplementedError

class Email(Notificacion):
    def enviar(self, mensaje):
        print(f"[Email] {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje):
        print(f"[SMS] {mensaje}")

class NotificacionFactory:
    @staticmethod
    def crear(tipo):
        if tipo == "email":
            return Email()
        elif tipo == "sms":
            return SMS()
        raise ValueError("Tipo no soportado")

if __name__ == "__main__":
    n = NotificacionFactory.crear("email")
    n.enviar("Hola desde el patrón Factory")