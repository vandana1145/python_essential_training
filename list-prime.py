import isprime

def list_prime():
    for i in range(100):
        if isprime(i):
            print(i, end=' ', flush=True)
    print()


list_prime()