import random

def generate_unique_random_numbers(n):
    if n > 0:
        return random.sample(range(1, n * 10), n)  # Generates n unique random numbers between 1 and n*10
    else:
        return []

# Generate 50 unique random numbers
random_numbers = generate_unique_random_numbers(50)
print(random_numbers)
