def make_car(fabricante,modelo,**car_info):
    car_info['fabricante'] = fabricante
    car_info['modelo'] = modelo
    return car_info

coches = []
coches.append(make_car('subaru','impreza',color='blue',tow_package='True'))
coches.append(make_car('peugeot','308',color='blaco',tow_package='True'))
coches.append(make_car('ferrari','enzo',color='red',tow_package='False'))

for car in coches:
    print(car)