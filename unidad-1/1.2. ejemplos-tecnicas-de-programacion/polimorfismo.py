class SistemaNotificacion:
    def enviar_notificacion(self, mensaje):
        pass

class NotificacionEmail(SistemaNotificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando email: {mensaje}")

class NotificacionSMS(SistemaNotificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando SMS: {mensaje}")

class NotificacionWhatsApp(SistemaNotificacion):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando WhatsApp: {mensaje}")

# Demostración de polimorfismo
def enviar_multiples_notificaciones(notificaciones, mensaje):
    for notificacion in notificaciones:
        notificacion.enviar_notificacion(mensaje)

# Uso del polimorfismo
notificaciones = [
    NotificacionEmail(),
    NotificacionSMS(),
    NotificacionWhatsApp()
]

enviar_multiples_notificaciones(notificaciones, "¡Hola mundo!")