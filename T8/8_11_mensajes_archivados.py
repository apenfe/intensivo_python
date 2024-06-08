def enviar_mensajes(mensajes):
    salida = []
    while mensajes:
        mensaje_actual = mensajes.pop()
        print(mensaje_actual)
        salida.append(mensaje_actual)
    return salida

mensajes = ['Hola','a','todos']
impresos = enviar_mensajes(mensajes[:])

print(impresos)
print(mensajes)