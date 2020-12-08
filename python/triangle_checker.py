# Checks what type of triangle the 3 sides form
def triangle(a, b, c):
    # Put the sides into a sorted array, so the shorter 2 sides come first
    sides = [a, b, c]
    sides.sort()
    # If the sides don't fulfill the triangle inequality (a + b > c),
    # these side lengths can't form a triangle
    if sides[0] + sides[1] <= sides[2]:
        return "Not a triangle"
    # If a^2 + b^2 < c^2, this is an obtuse triangle
    if sides[0] ** 2 + sides[1] ** 2 < sides[2] ** 2:
        return "Obtuse triangle"
    # If a^2 + b^2 > c^2, this is an acute triangle
    if sides[0] ** 2 + sides[1] ** 2 > sides[2] ** 2:
        return "Acute triangle"
    # Otherwise, a^2 + b^2 = c^2, so this is a right triangle
    return "Right triangle"


# Input 3 side lengths, and output the type of triangle they form
a = int(input("Enter the first side length: "))
b = int(input("Enter the second side length: "))
c = int(input("Enter the third side length: "))
print(triangle(a, b, c))
