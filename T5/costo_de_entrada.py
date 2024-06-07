edad = int(input('Digite sua edad: '))

tarifa_plana = 10

if edad >= 71:
    tarifa = tarifa_plana - tarifa_plana*10/100
    print(f'Su tarifa es de: {tarifa} dolares')
elif edad >= 56:
    tarifa = tarifa_plana - tarifa_plana * 5 / 100
    print(f'Su tarifa es de: {tarifa} dolares')
elif (edad >= 5) and (edad <= 17):
    tarifa = tarifa_plana - tarifa_plana*20/100
    print(f'Su tarifa es de: {tarifa} dolares')
elif edad < 5:
    tarifa = tarifa_plana - tarifa_plana*50/100
    print(f'Su tarifa es de: {tarifa} dolares')
