#Python program to find type of coin would represent that amount with the fewest total number of coins

cents = int(input("How many cents do you have? "))

# ct variable for cents

ct = cents
# use interger division of 25 to find quarters (q)
Q = cents // 25

cents -= (Q*25)

# use interger division of 25 to find dimes (d)

D = cents // 10

cents -= (D * 10)

# use interger division of 5 to find quarters (q)

N = cents // 5

cents -= (N * 5)

# use interger division of 1 to find quarters (q)

P = cents // 1

print("With " +str(ct)+ " cents you can have "+str(Q)+" quarters, "+str(D)+ " dimes, "+str(N)+" nickels, "+str(P)+" pennies.")

