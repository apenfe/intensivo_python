import glob
import os
import re

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

def extraer_categoria(tweet):

    if re.search("N$",tweet):
        cat = "N"
    elif re.search("P$",tweet):
        cat= "P"
    elif re.search("NEU$",tweet):
        cat = "NEU"

    return cat


def limpiar_tweet(tweet):

    tweet = re.sub("\d{18}\t", "", tweet)
    tweet = re.sub("@\w+", "", tweet)
    tweet = re.sub("#\w+", "", tweet)
    tweet = re.sub("\w*\d\w*", "", tweet)
    tweet = re.sub("[!¡?¿'\"&%()/*{};:.,-]+", "", tweet)
    tweet = re.sub("//t.co/(\w)+", "", tweet)
    tweet = re.sub("\n+", "", tweet)
    tweet = re.sub("\tN$|\tNEU$|\tP$", "", tweet)
    tweet = tweet.strip()
    tweet = tweet.lower()

    return tweet

# Categorías
y_train = list(map(extraer_categoria, train_raw))
y_test = list(map(extraer_categoria, test_raw))

# Tweets pre-procesados
x_train = list(map(limpiar_tweet, train_raw))
x_test = list(map(limpiar_tweet, test_raw))

# Ejemplos
# idx = 800 # 800, 1200, 600, 153
# print(f'Tweet original: {train_raw[idx]}')
# print(f'Tweet pre-procesado: {x_train[idx]} /// Categoría: {y_train[idx]}')

# stop_words_dic
def dic_stop_words(tweets):
    # Crear el diccionario
    dicc = {}

    # Iterar sobre cada tweet, extraer palabras e incluirlas en
    # el diccionario junto con su frecuencia
    for tweet in tweets:
        for word in tweet.split(' '):
            if word in dicc:
                dicc[word] += 1
            else:
                dicc[word] = 1

    # Y organizarlo de forma descendente (de las palabras más comunes
    # a las menos comunes)
    dicc_sorted = {}
    for k, v in sorted(dicc.items(), key=lambda item: item[1], reverse=True):
        dicc_sorted[k] = v

    return dicc_sorted

stop_words_dic = dic_stop_words(x_train)

# Y crear el listado de stop_words: las top-20 en stop_words_dic:
stop_words = list(stop_words_dic.keys())[0:35]

#  Ahora crear diccionarios para comentarios positivos, neutrales y
# negativos. No incluir palabras en "stop_word"

def dic_palabras_comunes(tweets, cats, categoria, stopwords):
    dicc = {}

    for tweet, cat in zip(tweets, cats):
        if cat == categoria:
            for word in tweet.split(' '):
                if word not in stopwords:
                    if word in dicc:
                        dicc[word] += 1
                    else:
                        dicc[word] = 1

    # Y organizarlo de forma descendente (de las palabras más comunes
    #  a las menos comunes
    dicc_sorted = {}
    for k, v in sorted(dicc.items(), key=lambda item: item[1], reverse=True):
        dicc_sorted[k] = v

    return dicc_sorted

positivos_dic = dic_palabras_comunes(x_train, y_train, 'P', stop_words)
negativos_dic = dic_palabras_comunes(x_train, y_train, 'N', stop_words)
neutrales_dic = dic_palabras_comunes(x_train, y_train, 'NEU', stop_words)

# Generemos los tres listados: positivos
positivos = list(positivos_dic.keys())

# Negativos: negativos - positivos
negativos = list(negativos_dic.keys())
negativos = set(negativos) - set(positivos)
negativos = list(negativos)

# Neutrales: neutrales - negativos - positivos
neutrales = list(neutrales_dic.keys())
neutrales = set(neutrales) - set(negativos) - set(positivos)
neutrales = list(neutrales)
