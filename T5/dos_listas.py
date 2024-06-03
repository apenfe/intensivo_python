ingredientes_disponibles = ['lechuga','tomate','salsa']

ingredientes_solicitados = ['lechuga','tomate','pollo']

for ingrediente_solicitado in ingredientes_solicitados:

    if ingrediente_solicitado in ingredientes_disponibles:
        print(f"añadiendo {ingrediente_solicitado}")
    else:
        print(f"Ese ingrediente no esta disponible: {ingrediente_solicitado}")
        
print("pizza terminada")