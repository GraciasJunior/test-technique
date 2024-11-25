# retourne la sous chaine la plus longue d'une chaine de caratère
def longest_unique_substring(s):
    n = len(s)
    res = 0
    for i in range(n):
        watchedChar = [False] * 256
        for j in range(i,n):
            if watchedChar[ord(s[j])] == True:
                break
            else:
                res = max(res,j-i+1)
                watchedChar[ord(s[j])] = True
    return res