import re

def eliminar_enlaces(texto):
    # Patrón de expresión regular para encontrar enlaces
    patron_enlace = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    
    # Utilizar re.sub para reemplazar los enlaces con una cadena vacía
    texto_sin_enlaces = re.sub(patron_enlace, '', texto)
    
    return texto_sin_enlaces

# Ejemplo de uso
texto_con_enlaces = "Es un buen profe y los documentos los revisa en LaTex, les dejo un curso por si no le saben https://ww.udemy.com/course/documentos-en-latex-con-autocad-adobe-acrobat-e-illustrator/?ranMID=39197&ranEAID=d2gvurItCFk&ranSiteID=d2gvurItCFk-q_YbjEbVG59oHxdBIqRn7A&LSNPUBID=d2gvurItCFk&utm_source=aff-cam. Es de hueva su clase. No dejes sus trabajos al final porque si son algo largos. No hay examen, a veces toma asistencia, las clases llegan a ser cansadas por"
texto_sin_enlaces = eliminar_enlaces(texto_con_enlaces)

print("Texto original:")
print(texto_con_enlaces)

print("\nTexto sin enlaces:")
print(texto_sin_enlaces)
