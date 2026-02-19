import itertools

letters = ('S','E','N','D','M','O','R','Y')
digits = range(10)

for perm in itertools.permutations(digits, 8):
    S,E,N,D,M,O,R,Y = perm

    if S == 0 or M == 0:
        continue

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    if send + more == money:
        print("\nSolution Found:\n")
        print("S =", S)
        print("E =", E)
        print("N =", N)
        print("D =", D)
        print("M =", M)
        print("O =", O)
        print("R =", R)
        print("Y =", Y)
        print("\nSEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break

