def triangle(a, b, c):
  sides = [a, b, c]
  sides.sort()
  if sides[0] + sides[1] <= sides[2]:
    return "Not a triangle"
  if sides[0]**2 + sides[1]**2 < sides[2]**2:
    return "Acute triangle"
  if sides[0]**2 + sides[1]**2 > sides[2]**2:
    return "Obtuse triangle"
  return "Right triangle"

a = int(input())
b = int(input())
c = int(input())
print(triangle(a, b, c))
