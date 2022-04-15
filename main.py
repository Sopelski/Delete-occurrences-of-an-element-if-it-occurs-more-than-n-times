'''Given a list and a number, create a new list that contains each number of lst at most N times without reordering.'''

def delete_nth(order,max_e):
    lista = []
    slownik = {}
    for liczba in order:
        if liczba in slownik:
            slownik[liczba] += 1
        else:
            slownik[liczba] = 1
        if slownik[liczba] <= max_e:
            lista.append(liczba)


    return print(lista)


delete_nth([1,1,3,3,7,2,2,2,2], 3)