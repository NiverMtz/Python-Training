texto = {1: "uno / um / one",
         2: "dos / dois / two",
         3: "tres / três / three",
         4: "cuatro / quatro / four",
         5: "cinco / cinco / five"}

espaniol = []
portugues = []
ingles = []


def myfunc():
    global espaniol, ingles, portugues
    for e in texto:
        aux = texto[e].split(" / ")
        espaniol.append(aux[0])
        portugues.append(aux[1])
        ingles.append(aux[2])


myfunc()

numeros = list(zip(espaniol, portugues, ingles))
