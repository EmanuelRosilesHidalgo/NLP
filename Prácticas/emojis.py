import re

# Texto de ejemplo que contiene emojis
texto = "Hola, 😃 ¿Cómo estás? 🌟"

# Patrón de expresión regular para detectar emojis
patron_emoji = '[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U0001FB00-\U0001FBFF\U0001F004\U0001F0CF\U0001F170-\U0001F251\U00002702]'
emojis = re.findall(patron_emoji, texto)

# Imprimir emojis encontrados
print("Emojis encontrados:")
for emoji in emojis:
    print(emoji)