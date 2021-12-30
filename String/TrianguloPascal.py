import math


def combination(n, r): # cálculo correcto de combinaciones
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascals_triangle(rows):
    result = [] # recopilar resultados
    for count in range(rows): 
        row = [] # necesita un elemento de fila
        for element in range(count + 1): 
            # coloca los elementos
            row.append(combination(count, element))
        result.append(row)
    return result

# imprimimos los resultados 
for row in pascals_triangle(5):
    print(row)
