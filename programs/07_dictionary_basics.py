"""
Program 7: Dictionary basics – create, access, update, delete a student record
Concept: Dictionaries (creation, access, update, deletion)
"""

def student_record_demo():
    """Demonstrate basic dictionary operations with a student record."""
    
    # Create a student record dictionary
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "year": "Sophomore"
    }
    
    print("Initial student record:")
    print(student)
    print()
    
    # Access values
    print("Accessing values:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"GPA: {student['gpa']}")
    print()
    
    # Update values
    print("Updating values:")
    student["gpa"] = 3.9  # Update GPA
    student["year"] = "Junior"  # Update year
    print(f"Updated GPA: {student['gpa']}")
    print(f"Updated year: {student['year']}")
    print()
    
    # Add new key-value pair
    print("Adding new information:")
    student["email"] = "alice.johnson@email.com"
    print(f"Added email: {student['email']}")
    print()
    
    # Delete a key-value pair
    print("Deleting information:")
    deleted_age = student.pop("age")  # Remove and return the age
    print(f"Removed age: {deleted_age}")
    print(f"Student record after deletion: {student}")
    print()
    
    # Check if key exists
    print("Checking key existence:")
    print(f"Has 'major' key: {'major' in student}")
    print(f"Has 'age' key: {'age' in student}")
    print()
    
    # Get all keys and values
    print("All keys:", list(student.keys()))
    print("All values:", list(student.values()))
    print("All items:", list(student.items()))

if __name__ == "__main__":
    student_record_demo()