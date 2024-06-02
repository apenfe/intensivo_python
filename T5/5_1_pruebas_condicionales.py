edad =7

if edad<18:
    print("Edad invalida")
else:
    print("Puedes pasar")

baneados =['lucia', 'tomas']
nombres = ['lucia','paco','tomas','raul']
edades = [18,22,3,23]

for i in range(0,len(edades)):

    if (edades[i]>=18) and nombres[i] not in baneados:
        print("Bienvenido")
    else:
        print("No pueden pasar menores de edad")