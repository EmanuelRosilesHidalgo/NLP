import json
import re
import textwrap

#import phunspell

filename = 'comentarios_profesores_ver1.json'
"""dictionary = phunspell.Phunspell('es_MX')
en_dictionary = phunspell.Phunspell('en_US')"""


def correct_spelling(text):
    list = text.split(" ")
    errors = dictionary.lookup_list(list)
    errors = en_dictionary.lookup_list(errors)
    print(text)
    if errors:
        for error in errors:
            if '.' not in error and ',' not in error and len(error) < 14 and not error.isupper():
                print(error)
                i: int = list.index(error)
                suggestions = []
                for suggestion in dictionary.suggest(error):
                    suggestions.append(suggestion)
                    break
                if suggestions:
                    print(suggestions)
                    list[i] = suggestions[0]
        errors.clear()
        text = ""
        for word in list:
            text = text + word + " "
        list.clear()
    print(text)
    return text


def delete_repeated(text):
    print(type(text))
    text_list = [*text]
    repeated = []
    text_new = []
    c = ""
    for char in text_list:
        c = char
        if repeated:
            if repeated[0] == char:
                repeated.append(char)
            else:
                if repeated.__len__() == 1:
                    text_new.append(repeated[0])
                else:
                    for e in range(2):
                        text_new.append(repeated[e])
                repeated.clear()
                repeated.append(char)
        else:
            repeated.append(char)
    text_new.append(c)
    text = ""
    for char in text_new:
        text = text + char
    return text


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
#print(json_data[7]["Comentarios"])
texto2 = ' '.join(json_data[52]["Nombre"])
print(texto2)




# json_data.pop(0)
# cond = "[Comentario esperando revisión]"
# json_data = delete_comment(json_data, cond)


"""
Quitar saltos de línea
Eliminar emoticones
"""


def delete_pattern(data):
    """
    emogi = re.compile("[\u263a-\U0001f645]")
    e1 = re.compile("\s\W?:[\w\W][\w\W]?")
    e2 = re.compile("\s[xX][dD]")
    e3 = re.compile("\s</?3")
    """
    e4 = re.compile("\s[uU][wW][uU]")
    index = 0
    for entry in data:
        lista_temp = []
        for comment in entry["Comentarios"]:
            """
            comment = re.sub("\n", " ", comment)
            comment = re.sub(e1, "", comment)
            comment = re.sub(e2, "", comment)
            comment = re.sub(e3, "", comment)
            comment = re.sub(emogi, "", comment)
            """
            comment = re.sub(e4, "", comment)
            lista_temp.append(comment)
        print(data[index]["Nombre"])
        data[index]["Comentarios"] = lista_temp.copy()
        lista_temp.clear()
        index += 1
    return data


# json_data = delete_pattern(json_data)
"""Eliminar signos muy repetidos"""


def delete_reps_from_comments(data):
    index = 0
    for entry in data:
        print(data[index]["Nombre"])
        lista_temp = []
        i = 0
        for comment in entry["Comentarios"]:
            comment = delete_repeated(comment)
            lista_temp.append(comment)
            print(i)
            i += 1
        data[index]["Comentarios"] = lista_temp.copy()
        lista_temp.clear()
        index += 1
    return data


# json_data = delete_reps_from_comments(json_data)
"""Eliminar palabras mal escritas"""


def correct_comments(data):
    index = 0
    for entry in data:
        print(data[index]["Nombre"])
        lista_temp = []
        i = 0
        for comment in entry["Comentarios"]:
            comment = correct_spelling(comment)
            lista_temp.append(comment)
            print(i)
            i += 1
        data[index]["Comentarios"] = lista_temp.copy()
        lista_temp.clear()
        index += 1
    return data


#json_data = correct_comments(json_data)
#save_data("comentarios_profesores_ver2.json", json_data)
