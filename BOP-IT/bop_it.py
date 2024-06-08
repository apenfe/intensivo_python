import funciones as f
from threading import Timer

puntaje = 0
timeout = 3
delta = 0.1
succes = True

while succes:

    estado = f.seleccionar_estado()
    t = Timer(timeout, print, 'Se acabó el tiempo')
    t.start()
    f.comando_voz(estado)
    succes = f.interaccion_usuario(estado)
    t.cancel()

    if t.is_alive() == False:  # si termina la cuanta regresiva sin interaccion
        break
    # si el usuario responde correctamente sumar puntos y reducir tiempo
    if succes:
        puntaje += 1

        if timeout - delta > 0:
            timeout -= delta
    else:
        print("fallaste")

print(f"puntuaje final: {puntaje}")
