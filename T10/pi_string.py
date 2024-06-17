from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()

pi_string = ''

for line in lines:

    pi_string += line.rstrip()

birthday = input('Inserte su cumpleaños en formato ddmmaa: ')

if birthday in pi_string:
    print("tu fecha de cumpleaños esta en pi")
else:
    print("Tu fecha de cumpleñaos no está en pi")