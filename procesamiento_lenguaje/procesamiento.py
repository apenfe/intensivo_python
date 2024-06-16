import glob
import os

train_raw = []
print(f"Leyendo set de entrenamiento...")

directory_path = os.path.join(".", "datasets", "train", "*.tsv")

for filename in glob.glob(directory_path):
    print(f"\t{filename}")
    print("\t"+"-"*25)
    with open(filename,'r',encoding='utf-8') as f:
        for line in f:
            train_raw.append(line)

print(f"\tTotal datos de entrenamiento: {len(train_raw)}")

test_raw = []
for filename in glob.glob(".\\datasets\\dev\\*.tsv"):
    print(f"\t{filename}")
    print("\t" + "-" * 25)
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            test_raw.append(line)

print(f"\tTotal datos de prueba: {len(test_raw)}")