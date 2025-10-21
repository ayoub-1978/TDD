# exo2.py
import string

# Table complète selon l'énoncé
caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message):
    resultat = ""
    for char in message:
        if char in caracteres:
            index = caracteres.index(char)
            # on prend le caractère suivant, et on boucle si on atteint la fin
            resultat += caracteres[(index + 1) % len(caracteres)]
        else:
            # caractères non listés sont inchangés
            resultat += char
    return resultat
