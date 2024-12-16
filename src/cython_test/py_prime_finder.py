def py_prime_finder(amount: int) -> list[int]:
    primes: list[int] = []
    amount = min(amount, 100000)
    found = 0
    number = 2

    while found < amount:
        for x in primes[:found]:
            if number % x == 0:
                break
        else:
            primes.append(number)
            found += 1
        number += 1
    return [p for p in primes[:found]]
