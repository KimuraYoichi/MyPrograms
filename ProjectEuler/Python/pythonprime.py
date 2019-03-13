from sympy import prime
from sympy import sieve
from sympy import nextprime
from sympy import isprime

print(prime(10))

print([i for i in sieve.primerange(7,23)])

print(nextprime(123))
print(nextprime(127))


print(isprime(67280421310721))

for i in range(100):
    print(nextprime(i))