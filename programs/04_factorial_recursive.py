"""
Program 4: Recursive factorial function
Concept: Recursion (base case, recursive step)
"""

def factorial(n):
    """
    Calculate factorial of n using recursion.
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: Factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive step: n! = n * (n-1)!
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test with factorial of 5
    num = 5
    result = factorial(num)
    print(f"Factorial of {num} = {result}")
    
    # Additional test cases
    print(f"Factorial of 0 = {factorial(0)}")
    print(f"Factorial of 3 = {factorial(3)}")