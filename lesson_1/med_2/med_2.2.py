# Triangle Sides

def triangle(side1, side2, side3):
    sides = sorted([side1, side2, side3])
    if 0 in sides or sum(sides[:2]) <= sides[2]:
        return 'invalid'

    set_sides = set(sides)

    if len(set_sides) == 1:
        return 'equilateral'
    elif len(set_sides) == 2:
        return 'isosceles'
    return 'scalene'


print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True