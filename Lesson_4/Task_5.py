

def rep(poly1):
    dictPoly = {}
    poly1 = poly1.replace(' + ', ' +').replace(' - ', ' -')
    poly1 = poly1.split()
    poly1: object = poly1[:-2]
    for i in range(len(poly1)):
        poly1[i] = poly1[i].replace('+', '').split('x**')
        dictPoly[int(poly1[i][1])] = int(poly1[i][0])
    return dictPoly

def sumPoly(dict1, dict2):
    dictFinal = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dictFinal[i] = (first if first != None else 0) + (second if second != None else 0)
    return dictFinal

def koefResult(dictFinal):
    result = ''
    for i in dictFinal.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x^' + str(abs(i[0]))
        result = result.replace('x^1 ', 'x ').replace('x^0', '').replace('1x^ ', 'x^')
    return result + ' = 0'

with open('mnogo_1.txt', 'r', encoding='utf-8') as text:
    poly1 = text.readline()
with open('mnogo_2.txt', 'r', encoding='utf-8') as text:
    poly2 = text.readline()
print(poly1)
print(poly2)
dictPoly1 = rep(poly1)
dictPoly2 = rep(poly2)
dictFinal = sumPoly(dictPoly1, dictPoly2)
dictFinal = koefResult(dictFinal)
print(dictFinal)
with open ('sum_mnogo.txt', 'w', encoding='utf-8') as text:
    text.writelines(dictFinal)
