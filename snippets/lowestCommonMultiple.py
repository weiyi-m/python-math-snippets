# Find the lowest common factor of a and b.

def lowestCommonMultiple(a, b):

    if a > b:
        greater = a
    else:
        greater = b

    while(True):
        if (greater % a == 0) and (greater % b == 0):
            lcm = greater
            break

        greater += 1

    print(lcm)

a = int(input("a: "))
b = int(input("b: "))

