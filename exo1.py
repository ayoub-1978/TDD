def affiche():
    def valeur_fizzbuzz(i):
        if i % 15 == 0:
            return "FrisBee"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        return str(i)

    print("".join(valeur_fizzbuzz(i) for i in range(1, 101)), end="")