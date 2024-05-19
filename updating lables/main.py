MOD = 998244353

def power(x, y):
    """ Computes (x^y) % MOD using exponentiation by squaring """
    r = 1
    x %= MOD
    while y:
        if y & 1:
            r = (r * x) % MOD
        y >>= 1
        x = (x * x) % MOD
    return r

# Read input values
m,k=5,1

# Initialize result variable
result = 0

# Array to store the smallest prime factor (SPF) for each number up to k
ei = [0] * (k + 1)

# List to store Mobius function values
bags = [0, 1]

# Compute the smallest prime factor for each number up to k
for i in range(2, k + 1):
    for j in range(i, k + 1, i):
        if ei[j] == 0:
            ei[j] = i

# Compute Mobius function values
for i in range(2, k + 1):
    if ei[i] == i:
        # i is a prime number
        bags.append(-1)
    else:
        if ei[i // ei[i]] == ei[i]:
            # i has a squared prime factor
            bags.append(0)
        else:
            # Compute Mobius value using previously computed values
            bags.append(-bags[i // ei[i]])

# Calculate the result using Mobius function values and the power function
for i in range(1, k + 1):
    term = (MOD + bags[i]) * (power((k // i) * 2 + 1, m) - 1) % MOD
    result = (result + term) % MOD

# Output the final result
print(result + 1)
