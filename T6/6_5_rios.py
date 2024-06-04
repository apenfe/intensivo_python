rios = {'ebro': 'spain','nilo':'egipto','danubio':'alemania','mississipi':'eeuu'}

for rio, pais in rios.items():
    print(f"El rio {rio.title()} transcurre por {pais}")

for rio in rios.keys():
    print(f"Rio {rio.title()}")

for pais in rios.values():
    print(f"Pais: {pais.title()}")