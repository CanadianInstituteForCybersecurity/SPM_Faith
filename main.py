def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def reverse_number(n):
    return int(str(n)[::-1])

def cumbersome_prime_task(limit):
    prime_dict = {}
    
    # Finding all primes and reversing them
    for num in range(2, limit + 1):
        if is_prime(num):
            reversed_num = reverse_number(num)
            prime_dict[num] = reversed_num

    # Display primes with their reversed value
    print("Prime numbers and their reverses:")
    for prime, reverse in prime_dict.items():
        print(f"{prime} -> {reverse}")

    # Calculate the sum of prime and its reverse
    result_sum = 0
    for prime, reverse in prime_dict.items():
        result_sum += prime + reverse

    return result_sum

# Set a limit for prime search
limit = 100
result = cumbersome_prime_task(limit)
print(f"\nSum of primes and their reverses: {result}")
