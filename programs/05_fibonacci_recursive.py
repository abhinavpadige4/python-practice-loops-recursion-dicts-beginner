"""
Program 5: Recursive Fibonacci (nth term)
Concept: Recursion (base case, recursive step)
"""

def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Note:
        Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, ...
        F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) for n > 1
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Recursive step: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    # Test with Fibonacci of 7 (should return 13)
    n = 7
    result = fibonacci(n)
    print(f"Fibonacci({n}) = {result}")
    
    # Show first few Fibonacci numbers for reference
    print("First 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci(i)}", end="   ")
    print()