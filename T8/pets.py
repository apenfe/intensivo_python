def describe_pet(animal_type,pet_name):
    print(f"\ntengo un {animal_type}")
    print(f"Mi {animal_type} se llama {pet_name}")

describe_pet("perro","zaira")
describe_pet("perro","laika")

describe_pet(animal_type="gato",pet_name="misifu")

def describe_pet_2(pet_name,animal_type='perro'):
    print(f"\ntengo un {animal_type}")
    print(f"Mi {animal_type} se llama {pet_name}")

describe_pet_2("pancho")