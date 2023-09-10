colors1 = {'red', 'green', 'blue'}
colors2 = {'cyan', 'green', 'blue', 'magenta', 'red'}

# 1. Comparing the sets using each of the comparison operators.
print("1. Comparisons:")
print("colors1 == colors2:", colors1 == colors2)
print("colors1 != colors2:", colors1 != colors2)
print("colors1 < colors2:", colors1 < colors2) # colors1 is a proper subset of colors2
print("colors1 <= colors2:", colors1 <= colors2) # colors1 is a subset of colors2
print("colors1 > colors2:", colors1 > colors2)
print("colors1 >= colors2:", colors1 >= colors2)

# 2. Combining the sets using each of the mathematical set operators.
print("\n2. Set Operations:")
print("Union:", colors1 | colors2)
print("Intersection:", colors1 & colors2)
print("Difference (colors1 - colors2):", colors1 - colors2)
print("Difference (colors2 - colors1):", colors2 - colors1)
print("Symmetric Difference:", colors1 ^ colors2)

# or
# colors1, colors2 = {'red', 'green', 'blue'}, {'cyan', 'green', 'blue', 'magenta', 'red'}
# print((colors1 == colors2, colors1 != colors2, colors1 < colors2, colors1 <= colors2, colors1 > colors2, colors1 >= colors2, colors1 | colors2, colors1 & colors2, colors1 - colors2, colors2 - colors1, colors1 ^ colors2))
