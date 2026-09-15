"""
Program 10: Loop over dictionary to find keys with values above threshold
Concept: Dictionaries (access, iteration) + Loops
"""

def find_high_scores(scores, threshold):
    """
    Find all keys (students) with scores above a given threshold.
    
    Args:
        scores: Dictionary with student names as keys and scores as values
        threshold: Minimum score to be considered "high"
        
    Returns:
        list: List of student names with scores above threshold
    """
    high_scorers = []
    
    # Loop through dictionary items
    for student, score in scores.items():
        if score > threshold:
            high_scorers.append(student)
    
    return high_scorers

def find_high_scores_with_scores(scores, threshold):
    """
    Find all students with scores above threshold and return their scores too.
    
    Args:
        scores: Dictionary with student names as keys and scores as values
        threshold: Minimum score to be considered "high"
        
    Returns:
        list: List of tuples (student_name, score) for scores above threshold
    """
    high_scorers = []
    
    # Loop through dictionary items
    for student, score in scores.items():
        if score > threshold:
            high_scorers.append((student, score))
    
    return high_scorers

if __name__ == "__main__":
    # Test with dictionary of scores
    test_scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96,
        "Eve": 83,
        "Frank": 79,
        "Grace": 91
    }
    
    threshold = 80
    
    print("Student Scores:")
    print("-" * 20)
    for student, score in test_scores.items():
        print(f"{student}: {score}")
    print()
    
    # Find students with scores above threshold
    high_scorers = find_high_scores(test_scores, threshold)
    print(f"Students with scores above {threshold}:")
    print("-" * 30)
    for student in high_scorers:
        print(f"{student}: {test_scores[student]}")
    print()
    
    # Alternative version returning tuples
    high_scorers_detailed = find_high_scores_with_scores(test_scores, threshold)
    print(f"Students with scores above {threshold} (detailed):")
    print("-" * 40)
    for student, score in high_scorers_detailed:
        print(f"{student}: {score}")
    print()
    
    # Test with different threshold
    threshold_90 = 90
    high_scorers_90 = find_high_scores(test_scores, threshold_90)
    print(f"Students with scores above {threshold_90}:")
    print("-" * 30)
    for student in high_scorers_90:
        print(f"{student}: {test_scores[student]}")