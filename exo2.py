import string

caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message, pas):
    """
    Cryptage du message :
    - Chaque caractère est décalé de 'pas' positions dans la table 'caracteres'
    - Le pas est concaténé à la fin du message crypté
    """
    def decale(c):
        if c in caracteres:
            i = caracteres.index(c)
            return caracteres[(i + pas) % len(caracteres)]
        return c  # caractère inconnu inchangé

    return "".join(decale(c) for c in message) + str(pas)