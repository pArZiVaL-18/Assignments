def parabola_vertex(a, b, c):
    h = -b / (2 * a)
    k = a * h**2 + b * h + c
    return (h, k)


a = 1
b = -4
c = 3

vertex = parabola_vertex(a, b, c)
print(vertex)
