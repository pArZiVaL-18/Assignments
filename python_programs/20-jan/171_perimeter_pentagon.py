def pentagon_perimeter_irregular(sides):
    if len(sides) != 5:
        print("A pentagon must have exactly 5 sides")
        return -1
    if any(side < 0 for side in sides):
        print("Side lengths cannot be negative")
    return sum(sides)


print(pentagon_perimeter_irregular([4, 5, 3, 6, 2]))
print(pentagon_perimeter_irregular([3, 2, 4,1]))