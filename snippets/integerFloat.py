# Is n an integer?

def integerFloat(n):
    if isinstance(n, int):
        print("True")
    else:
        print("False")

n = input("n: ")

integerFloat(n)