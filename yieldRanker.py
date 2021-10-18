




def normalizeData(data):

    max = max(values(data))

    for key in data:
        data[key] = data[key] / max

    return data










    







