def affiche(n):
    def fizzbuzz_value(i):
        if i % 15 == 0:
            return "FrisBee"
        elif i % 3 == 0:
            return "Fizz"
        elif i % 5 == 0:
            return "Buzz"
        return str(i)
    
    return "".join(fizzbuzz_value(i) for i in range(1, n + 1))
