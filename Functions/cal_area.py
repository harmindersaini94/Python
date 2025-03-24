def Area(radius):
    circum = radius * 2
    area = 3.14159 * (radius ** 2)
    return circum, area

print(Area(10))