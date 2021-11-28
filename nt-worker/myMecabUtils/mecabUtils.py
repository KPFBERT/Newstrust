def getNoun(val):
    result = []
    for temp in val:
        if temp[1] in 'NNG' or temp[1] in 'NNP' or temp[1] in 'NNB' or temp[1] in 'NNBC' or temp[1] in 'NR' or temp[
            1] in 'NP':
            result.append(temp[0])
    return result


def getVerb(val):
    result = []
    for temp in val:
        if temp[1] in 'VV' or temp[1] in 'VA' or temp[1] in 'VX' or temp[1] in 'VCP' or temp[1] in 'VCN':
            result.append(temp[0])
    return result


def getAdverb(val):
    result = []
    for temp in val:
        if temp[1] in 'MAG' or temp[1] in 'MAJ':
            result.append(temp[0])
    return result


def getForeignLanguage(val):
    result = []
    for temp in val:
        if temp[1] in 'SL' or temp[1] in 'SH':
            result.append(temp[0])
    return result
