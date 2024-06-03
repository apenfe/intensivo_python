edad = 12

if edad < 4:
    print("su coste de admision es 0")
elif edad < 18:
    print("su coste de admission es 25 $")
else:
    print("su coste de admission es 50 $")

edad = 18

if edad < 4:
    coste=0
elif edad < 18:
    coste=25
else:
    coste=50

print(f"su coste de admission es {coste} $")