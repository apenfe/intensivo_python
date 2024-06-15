def leer_texto(ruta):

    palabras = []
    with open(ruta, 'r', encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                palabras.append(word)

    return palabras

def calcular_frecuencias(words):

    frecuencias = {}

    for word in words:
        if word in frecuencias:
            frecuencias[word] += 1
        else:
            frecuencias[word] = 1

    return frecuencias

def ordenar_diccionario(freqs):

    freqs_sorted = {k:v for k, v in sorted(freqs.items(), key =lambda x: x[1], reverse=True)}
    return freqs_sorted

def diccionarios_cod_decod(freqs_sorted):

    tam_vocab = len(freqs_sorted)
    word2num = {k:v for k,v in zip(freqs_sorted.keys(), range(tam_vocab))}
    num2word = {v:k for k,v in word2num.items()}

    return word2num, num2word

palabras = leer_texto('quijote.txt')
frecuencias = calcular_frecuencias(palabras)
frecs_sorted = ordenar_diccionario(frecuencias)
word_to_num, num_to_word = diccionarios_cod_decod(frecs_sorted)

with open('quijote.txt','r',encoding='utf8') as fr, open('quijote_codificado.txt','w') as fw:
    for line in fr:
        for word in line.split():
            codigo = str(word_to_num[word]) + ' '
            fw.write(codigo)
        fw.write('\n')

fr.close()
fw.close()

with open('quijote_codificado.txt','r') as fr, open('quijote_decodificado.txt','w',encoding='utf8') as fw:
    for line in fr:
        for codigo in line.split():
            palabra = num_to_word[int(codigo)] + ' '
            fw.write(palabra)
        fw.write('\n')

fr.close()
fw.close()