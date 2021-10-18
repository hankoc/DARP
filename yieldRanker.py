


def normalizeData(data):

    tupleData = items(data) # tuple in the form (apr(int), poolName(string))

    aprData = []

    for i in tupleData:
        aprData.append(i[0])

    normalVector = []

    for i in tupleData:
        pair = (i[0] / max(aprData), i[1])
        normalVector.append(pair)

    return normalVector







    







