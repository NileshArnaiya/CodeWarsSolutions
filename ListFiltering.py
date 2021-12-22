def filter_list(l):
    newList = []

    for s in range(len(l)):
        if not(isinstance(l[s], str)):
            newList.append(l[s])
    return newList