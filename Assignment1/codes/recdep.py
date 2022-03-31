def rd(P, n, r) :
    MV = P * n + P * (n * (n + 1) / (2 * 12)) * (r / 100)
    return MV

P = 600
n = 2.5 * 12
r = 10

MV = rd(P, n, r)

print("The maturity value of the recurring deposit is", MV)
