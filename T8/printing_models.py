def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        cured_design = unprinted_designs.pop()
        print(f"Imprimiendo modelo: {cured_design}")
        completed_models.append(cured_design)

def show_completed_models(completed_models):
    print("Los siguientes modelos han sido impresos:")
    for completed in completed_models:
        print(completed)

unprinted_designs = ['phone case','robot pedant','dodecahedron']
completed_models = []

print_models(unprinted_designs[:],completed_models)
show_completed_models(completed_models)