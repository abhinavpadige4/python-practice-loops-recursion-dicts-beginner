# Python Beginner Practice: 10 Programs

This repository contains 10 Python practice programs designed for beginners to learn and reinforce core programming concepts including loops, recursion, and dictionaries.

## Programs Included

### 🔁 Loops
1. **01_print_numbers.py** - Simple for-loop to print numbers 1 to 10
2. **02_sum_while.py** - While-loop to compute sum of a list of integers  
3. **03_multiplication_table.py** - Nested for-loops to print a multiplication table (1-10)

### 🔄 Recursion
4. **04_factorial_recursive.py** - Recursive factorial function
5. **05_fibonacci_recursive.py** - Recursive Fibonacci (nth term)
6. **06_reverse_string_recursive.py** - Recursive string reversal

### 📚 Dictionaries
7. **07_dictionary_basics.py** - Dictionary basics – create, access, update, delete a student record
8. **08_word_frequency.py** - Count word frequencies in a sentence using a dictionary
9. **09_nested_dict_inventory.py** - Nest dictionaries – inventory of products with price and stock
10. **10_dict_loop_threshold.py** - Loop over dictionary to find keys with values above threshold

## Topics Covered

- **Loops**: for/while loops, nested loops, loop control
- **Recursion**: base case, recursive step, recursive functions, call stack
- **Dictionaries**: creation, access, update, deletion, nesting, iteration

## How to Run

Each program is a standalone Python file. To run any program:

```bash
python programs/01_print_numbers.py
```

Replace `01_print_numbers.py` with the desired program file.

To run all programs sequentially:
```bash
for file in programs/*.py; do
    echo "Running $file..."
    python "$file"
    echo "---"
done
```

## Requirements

- Python 3.8+

## Learning Objectives

By completing these exercises, you will:
- Understand and implement basic loop constructs (for, while, nested loops)
- Apply recursive thinking to solve problems with proper base cases
- Work with dictionaries for data storage, retrieval, and manipulation
- Develop problem-solving skills through practical coding exercises
- Learn to read, understand, and debug code

## Program Details

### Program 1: Print Numbers 1-10
Demonstrates basic for-loop syntax and the range() function.

### Program 2: Sum List with While-Loop
Shows while-loop usage with manual index control for list traversal.

### Program 3: Multiplication Table
Illustrates nested loops for creating 2D patterns and tables.

### Program 4: Factorial Recursion
Teaches recursion with a clear base case (0! = 1, 1! = 1) and recursive step.

### Program 5: Fibonacci Recursion
Shows recursive definition with two base cases and exponential recursion pattern.

### Program 6: String Reversal Recursion
Demonstrates recursion on strings with last-character-first approach.

### Program 7: Dictionary Basics
Covers creating, accessing, updating, deleting, and checking dictionary keys.

### Program 8: Word Frequency Counter
Combines loops and dictionaries to count occurrences of words in text.

### Program 9: Nested Dictionary Inventory
Shows how to structure complex data with dictionaries containing dictionaries.

### Program 10: Threshold Filtering
Demonstrates dictionary iteration and conditional filtering based on values.

Happy coding! 🐍