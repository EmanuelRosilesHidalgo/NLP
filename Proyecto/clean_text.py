import json
import re

filename = 'comentarios_profesores_semiclean.json'


def load_data(route: str):
    with open(route, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def save_data(route: str, data):
    with open(route, 'w', encoding="utf-8") as file:
        json.dump(data, file)


"""Eliminar comentarios en revisión *"""


def delete_comment(data, condition):
    index = 0
    for entry in data:
        lista_temp = []
        for comment in entry["Comentarios"]:
            if comment != condition:
                lista_temp.append(comment)
        print(data[index]["Nombre"])
        data[index]["Comentarios"] = lista_temp.copy()
        lista_temp.clear()
        index += 1
    return data


json_data = load_data(filename)
"""
json_data.pop(0)
cond = "[Comentario esperando revisión]"
json_data = delete_comment(json_data, cond)
"""

"""
Quitar saltos de línea
Eliminar emoticones
"""


def delete_pattern(data):
    emogi = re.compile("[\u263a-\U0001f645]")
    e1 = re.compile("\s\W?:[\w\W][\w\W]?")
    e2 = re.compile("\s[xX][dD]")
    e3 = re.compile("\s</?3")
    index = 0
    for entry in data:
        lista_temp = []
        for comment in entry["Comentarios"]:
            comment = re.sub("\n", " ", comment)
            """
            comment = re.sub(e1, "", comment)
            comment = re.sub(e2, "", comment)
            comment = re.sub(e3, "", comment)
            comment = re.sub(emogi, "", comment)
            """
            lista_temp.append(comment)
        print(data[index]["Nombre"])
        data[index]["Comentarios"] = lista_temp.copy()
        lista_temp.clear()
        index += 1
    return data

print(json_data[1]["Nombre"])
# json_data = delete_pattern(json_data)
"""Eliminar palabras mal escritas"""

"""Eliminar signos muy repetidos"""
# save_data(filename, json_data)
