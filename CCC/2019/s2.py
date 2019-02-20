def main():
    T = int(input())

    results = {}

    for _ in range(T):
        N = int(input())

        if N in results:
            print(results[N])
            continue

        lowest = N
        highest = N

        while True:
            #print(lowest, highest)
            if is_prime(lowest) and is_prime(highest):
                results[N] = str(lowest) + " " + str(highest)
                break

            lowest -= 1
            highest += 1

        print(results[N])


# from https://stackoverflow.com/questions/15285534/isprime-function-for-python-language
def is_prime(number):
    if number == 2 or number == 3: return True
    if number < 2 or number % 2 == 0: return False
    if number < 9:
        return True
    if number % 3 == 0:
        return False
    r = int(number ** 0.5)
    f = 5
    while f <= r:
        if number % f == 0:
            return False
        if number % (f + 2) == 0:
            return False
        f += 6
    return True


if __name__ == "__main__":
    main()
