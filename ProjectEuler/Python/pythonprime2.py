import itertools, functools, math

def prime_stream():
    stream = itertools.count(2)
    sieve = lambda x, y: x % y != 0

    while True:
        prime = next(stream)
        stream = filter(functools.partial(sieve, y=prime), stream)
        yield prime

if __name__ == '__main__':
    primes = prime_stream()
    for _ in range(20): print(next(primes))
