"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

with open("data.csv", "r") as file:
    x = file.readlines()

x = [row.replace("\n", "") for row in x]
x = [z.split("\t") for z in x]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    resultado = sum([int(z[1]) for z in x])
    return resultado


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    y = [z[0] for z in x]
    suma = [(z,y.count(z)) for z in sorted(set(y))]
    return suma


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    y = [z[0] for z in x]
    suma = [[z,0] for z in sorted(set(y))]
    for z in suma:
        for row in x:
            if row[0] == z[0]:
                z[1] += int(row[1])
    suma = [tuple(z) for z in suma]
    return suma


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    y = sorted([z[2].split("-")[1] for z in x])
    suma = [(z,y.count(z)) for z in sorted(set(y))]

    return suma


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    y = [z[0] for z in x]
    number = [z[1] for z in x]
    suma = [[z,int(min(number)),int(max(number))] for z in sorted(set(y))]
    for z in suma:
        for row in x:
            if row[0] == z[0]:
                if int(row[1]) > z[1]:
                    z[1] = int(row[1])
                if int(row[1]) < z[2]:
                    z[2] = int(row[1])
    
    suma = [tuple(z) for z in suma]    
    return suma


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    y = [z[4] for z in x]
    clave = []
    valor = []
    w = []
    for i in y:
        w.append(i.split(","))
        for z in w:
            for i in z:
                clave.append(i.split(":")[0])
                valor.append(i.split(":")[1])
    xx = list(zip(clave,valor))

    suma = [[z,int(max(valor)),int(min(valor))] for z in sorted(set(clave))]
    for z in suma:
        for row in xx:
            if row[0] == z[0]:
                if int(row[1]) > z[2]:
                    z[2] = int(row[1])
                if int(row[1]) < z[1]:
                    z[1] = int(row[1])
    
    suma = [tuple(z) for z in suma]   
    return suma


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    y = sorted(set([int(z[1]) for z in x]))
    lista = []

    for z in y:
        lista2 = []
        for i in x:
            if z == int(i[1]):
                lista2.append(i[0])
        lista.append(lista2)

    suma = list(zip(y,lista))
    return suma


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    y = sorted(set([int(z[1]) for z in x]))
    lista = []

    for z in y:
        lista2 = []
        for i in x:
            if z == int(i[1]) and i[0] not in lista2:
                lista2.append(i[0])
        lista2 = sorted(lista2)
        lista.append(lista2)

    suma = list(zip(y,lista))
    return suma


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    y = []
    y = [z[4] for z in x]
    clave = []
    w = []
    suma = {}

    for i in y:
        w.append(i.split(","))
    for j in w:
        for i in j:
            clave.append(i.split(":")[0])
    
    for o in [[p,clave.count(p)] for p in sorted(set(clave))]:
        key, value = o[0], o[1]
        suma[key] = value
    return suma


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]

    """
    y = ([z[0] for z in x])
    suma = [(o[0],len(o[3].split(",")),len(o[4].split(","))) for o in x]
    return suma


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """

    lista = []
    lista2 = []
    final = {}
    y = [[z[1],z[3].split(",")]for z in x]

    for n in y:
        for w in range(len(n[1])):
            lista.append(n[0])
        
    for n in y:
        lista2 = lista2 + n[1]
    
    xx = list(zip(lista2,lista))
    xxx = [z[0] for z in xx]
    suma = [[z,0] for z in sorted(set(xxx))]

    for z in suma:
        for row in xx:
            if row[0] == z[0]:
                z[1] += int(row[1])
    for o in [z for z in suma]:
        key, value = o[0], o[1]
        final[key] = value
    return final


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """

    y2 = [z[0] for z in x]
    y = [z[4] for z in x]
    w = []
    valor = []
    final = {}
    for i in y:
        w.append(i.split(","))
    for z in w:
        lista = []
        for i in z:
            lista.append(int(i.split(":")[1]))
        valor.append(sum(lista))
    
    xx = list(zip(y2,valor))
    xxx = [z[0] for z in xx]
    suma = [[z,0] for z in sorted(set(xxx))]

    for z in suma:
        for row in xx:
            if row[0] == z[0]:
                z[1] += int(row[1])
    for o in [z for z in suma]:
        key, value = o[0], o[1]
        final[key] = value
    return final



