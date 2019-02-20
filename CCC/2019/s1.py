flips = input()

horizontal = False
vertical = False

for flip in flips:
    # print(flip)
    if flip == "H":
        horizontal = not horizontal
    else:
        vertical = not vertical

if horizontal and vertical:
    print("4 3\n2 1")
elif horizontal:
    print("3 4\n1 2")
elif vertical:
    print("2 1\n4 3")
else:
    print("1 2\n3 4")
