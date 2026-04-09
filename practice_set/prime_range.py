def prime_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

if __name__ == "__main__":
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    prime_numbers = prime_range(start, end)
    print(f"Prime numbers between {start} and {end}: {prime_numbers}")
    print(f"Count of prime numbers between {start} and {end}: {len(prime_numbers)}")