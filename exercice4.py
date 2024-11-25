#nombres manquants dans une liste
def find_missing_number(lists):
    
    max = lists[0]
    for i in lists:
        if i > max:
            max = 1
    min = lists[0]
    for i in lists:
        if i < min:
            min = i
            
    list1 = []

    for num in range(min + 1, max):
        if num not in lists:
            list1.append(num)
    return list1


lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing_number(lst))