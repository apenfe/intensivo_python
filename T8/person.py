def build_person(first_name,last_name,age=None):
    person ={'first':first_name,"last":last_name}

    if age:
        person["age"]=age

    return person

musician = build_person("jimi","hendrix")
print(musician)

musician = build_person("jimi","hendrix", 28)
print(musician)