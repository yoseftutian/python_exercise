def is_fibonacci(number):
    """Checks whether a given number is a Fibonacci number using iterative generation."""

    if number < 0:
        return False  # Fibonacci numbers are non-negative

    # Initialize the first two Fibonacci numbers
    fib1 = 0
    fib2 = 1

    # Generate Fibonacci numbers until we find the given number or exceed it
    while fib2 < number:
        # Calculate the next Fibonacci number
        next_fib = fib1 + fib2
        fib1 = fib2
        fib2 = next_fib

    # Check if the given number is equal to the current Fibonacci number
    return fib2 == number


# Example usage
result = is_fibonacci(8)
print(result)


