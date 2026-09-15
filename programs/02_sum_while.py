"""
Program 2: While-loop to compute sum of a list of integers
Concept: Loops (while-loop)
"""

def sum_list_while(numbers):
    """
    Compute the sum of a list of integers using a while-loop.
    
    Args:
        numbers: List of integers
        
    Returns:
        int: Sum of all numbers in the list
    """
    total = 0
    index = 0
    
    while index < len(numbers):
        total += numbers[index]
        index += 1
    
    return total

if __name__ == "__main__":
    # Test with sample list [5, 10, 15]
    sample_list = [5, 10, 15]
    result = sum_list_while(sample_list)
    print(f"Sum of {sample_list} = {result}")