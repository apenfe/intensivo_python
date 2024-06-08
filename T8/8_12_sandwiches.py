def sandwich(*elementos):
    print(f"ingredientes del sandwich: ")
    for elemento in elementos:
        print(elemento)

sandwich('jamon')
sandwich('jamon','queso')
sandwich('jamon','queso','huevo frito')