import concurrent.futures
import datetime
import math
import platform

def check_is_prime(n):
    print(f'testing {n}')
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor((math.sqrt(n))))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

PRIMES=[100000000000000003,100000000000000013,100000000000000019]
def main():
    t0 = datetime.datetime.now()
    for n in PRIMES:
        is_prime=check_is_prime(n)
        if is_prime:
            print(f'{n} {is_prime}')

    t1=datetime.datetime.now()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        a=executor.map(check_is_prime, PRIMES)
        for number, is_prime in zip(PRIMES, executor.map(check_is_prime, PRIMES)):
            if is_prime:
                print(f'{number} s_prime={is_prime}')
    print(f'{t1-t0} {datetime.datetime.now()-t1}')


if __name__=='__main__':
    main()
