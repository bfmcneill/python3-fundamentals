import timeit

from prime_sieve import is_prime, prime_sieve

def entrypoint():
    x = prime_sieve(1000)
    print(x)
    print(sum(x))



if __name__ == "__main__":
    entrypoint()