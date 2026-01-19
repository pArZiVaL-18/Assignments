import math

def regular_polygon_area(n, s):
    if n < 3 or s <= 0:
        return 0

    area = (n * s * s) / (4 * math.tan(math.pi / n))
    return area

print(regular_polygon_area(5, 6))   
print(regular_polygon_area(4, 5))   
print(regular_polygon_area(2, 4))
