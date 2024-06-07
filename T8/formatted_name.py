def get_formatted_name(first_name,middle_name,last_name=""):
    full_name = first_name + " " + middle_name + " " + last_name
    return full_name.title()

musician = get_formatted_name("jimi","hendrix")
print(musician)

musician = get_formatted_name("Adrian","peñalver","fernandez")
print(musician)