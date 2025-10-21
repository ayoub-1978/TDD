import string

# Table complète selon l'énoncé : lettres, ponctuation, chiffres, espace
caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message, pas):
    """
    Cryptage du message :
    - Chaque caractère du message est décalé de 'pas' positions dans la table 'caracteres'
    - Le pas est ajouté à la fin du message crypté
    """
    return "".join(
        caracteres[(caracteres.index(c) + pas) % len(caracteres)] if c in caracteres else c
        for c in message
    ) + str(pas)
