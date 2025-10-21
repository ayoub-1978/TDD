import string

caracteres = string.ascii_letters + string.punctuation + string.digits + " "

def crypt(message):
    def suivant(c):
        if c in caracteres:
            i = caracteres.index(c)
            return caracteres[(i + 1) % len(caracteres)]
        return c  # caractère inconnu inchangé
    return "".join(suivant(c) for c in message)
