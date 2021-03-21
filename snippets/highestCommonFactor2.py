# Find the HCF of a and b using the listing method

def highestCommonFactor2(a, b):
    alist = []
    blist = []

    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)

    for j in range(1, b + 1):
        if b % j == 0:
            blist.append(j)

    set_alist = set(alist)
    common_factors = set_alist.intersection(blist)
    commonfactors_list = list(common_factors)

    hcf = max(commonfactors_list)   

    print(hcf)

a = int(input("a: "))
b = int(input("b: "))

highestCommonFactor2(a, b)