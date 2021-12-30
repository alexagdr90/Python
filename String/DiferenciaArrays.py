# resta una lista de otra y devuelve el resultado.

array_diff = lambda a, b: [ i for i in a if i not in b]
a=[1, 22, 3, 3]
b=[1]
print(array_diff(a,b))
