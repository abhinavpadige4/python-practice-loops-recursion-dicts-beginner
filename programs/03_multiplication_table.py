"""
Program 3: Nested for-loops to print a multiplication table (1-10)
Concept: Loops (nested for-loops)
"""

def print_multiplication_table():
    """Print a 10x10 multiplication table using nested for-loops."""
    print("Multiplication Table (1-10):")
    print("-" * 40)
    
    for i in range(1, 11):
        for j in range(1, 11):
            product = i * j
            # Format output to align properly
            print(f"{i} x {j} = {product:2}", end="   ")
        print()  # New line after each row

if __name__ == "__main__":
    print_multiplication_table()