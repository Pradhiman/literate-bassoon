from math import*
a = 48


def is_prime(a):

    for i in range(2, floor(sqrt(abs(a))) + 1):
        if a % i == 0:
            return ["number is not prime", 0]
            break
    if a == 1:
        return ["number is not prime", 0]
    return ["number is prime", 1]


def factors(a):
    b = abs(a)
    factor = [b]
    for i in range(1, int(b / 2) + 1):
        if a % i == 0:
            factor.append(i)
    factor.sort()
    factor_str = map(str, factor)
    factors = ', '.join(factor_str)
    return [factor, factors]


def factorisation(a):
    p = abs(a)
    power_list = [0, "", "\u00B2", "\u00B3", "\u2074",
                  "\u2075", "\u2076", "\u2077", "\u2078", "\u2079"]
    prime_list = []
    while p >= 3:
        for index, subject in enumerate(factors(p)[0]):
            if is_prime(subject)[1] == 1:
                p = p / subject
                prime_list.append(subject)

    if p < 3:
        if not p == 1:
            prime_list.insert(0, p)
    set_1 = set(prime_list)
    list_1 = list(set_1)
    if 1 in list_1:
        list_1.remove(1)
    list_1.sort()

    prime_factor = []
    for i, s in enumerate(list_1):
        p = prime_list.count(s)
        prime_factor.append(str(s) + power_list[p])

    prime_factors = ' x '.join(prime_factor)

    return prime_factors


print(is_prime(a)[0])
if factors(a):
    print("no. of factors are ", len(factors(a)[0]))
    print("factors are ", factors(a)[1])
print("prime factorisation: ", factorisation(a))
