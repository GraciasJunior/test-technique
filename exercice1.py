#return la somme des chiffres d'un entier positif
def sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum+=int(digit)
    return sum

#n = 1111
#print(sum_of_digits(n))