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

def decrypt(message):
    """
    Décrypte un message généré par crypt(message, pas)
    - Le dernier caractère du message correspond au pas
    """
    # Récupérer le pas à partir du dernier caractère
    pas = int(message[-1])
    contenu = message[:-1]

    resultat = ""
    for c in contenu:
        if c in caracteres:
            i = caracteres.index(c)
            # Décalage inverse
            resultat += caracteres[(i - pas) % len(caracteres)]
        else:
            resultat += c
    return resultat