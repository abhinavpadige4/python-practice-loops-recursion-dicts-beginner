"""
Program 6: Recursive string reversal
Concept: Recursion (base case, recursive step)
"""

def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s: Input string
        
    Returns:
        str: Reversed string
    """
    # Base case: empty string or single character
    if len(s) <= 1:
        return s
    
    # Recursive step: last character + reverse of remaining string
    return s[-1] + reverse_string(s[:-1])

if __name__ == "__main__":
    # Test with input 'hello'
    test_string = "hello"
    reversed_string = reverse_string(test_string)
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reversed_string}'")
    
    # Additional test cases
    test_cases = ["", "a", "world", "Python", "recursion"]
    for test in test_cases:
        print(f"'{test}' -> '{reverse_string(test)}'")