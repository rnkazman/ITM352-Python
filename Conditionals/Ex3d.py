def determine_progress_no_if(hits, spins):
    """
    Alternative implementation of determine_progress1 using list indexing instead of if-statements.
    Uses boolean expressions to compute an index into a progress messages list.
    """
    # Handle the special case of 0 spins using short-circuit evaluation
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    # Progress messages list - ordered from least to most progress
    progress_messages = [
        "Get going!",      # index 0: ratio <= 0
        "On your way!",    # index 1: 0 < ratio < 0.25
        "Almost there!",   # index 2: 0.25 <= ratio < 0.5
        "You win!"         # index 3: ratio >= 0.5 and hits >= spins
    ]
    
    # Compute index using boolean expressions converted to integers
    # Each condition adds 1 to the index if true
    index = (
        int(hits_spins_ratio > 0) +           # +1 if ratio > 0
        int(hits_spins_ratio >= 0.25) +      # +1 if ratio >= 0.25
        int(hits_spins_ratio >= 0.5 and hits >= spins)  # +1 if ratio >= 0.5 AND hits >= spins
    )
    
    return progress_messages[index]


def determine_progress_no_if_v2(hits, spins):
    """
    Even more compact version using mathematical operations and list comprehension.
    """
    if spins == 0:
        return "Get going!"
    
    ratio = hits / spins
    messages = ["Get going!", "On your way!", "Almost there!", "You win!"]
    
    # Use sum of boolean conditions as index
    index = sum([
        ratio > 0,
        ratio >= 0.25,
        ratio >= 0.5 and hits >= spins
    ])
    
    return messages[index]


def determine_progress_no_if_v3(hits, spins):
    """
    Most compact version using a single expression.
    """
    return ("Get going!" if spins == 0 else
            ["Get going!", "On your way!", "Almost there!", "You win!"]
            [int(hits/spins > 0) + int(hits/spins >= 0.25) + int(hits/spins >= 0.5 and hits >= spins)])


# Test function to verify all versions work the same
def test_all_versions():
    # Import the original function for comparison
    import sys
    import os
    sys.path.append(os.path.dirname(__file__))
    
    # Test cases
    test_cases = [
        (10, 0),   # "Get going!" - no spins
        (0, 5),    # "Get going!" - no hits
        (1, 5),    # "On your way!" - 20% hit rate
        (2, 5),    # "Almost there!" - 40% hit rate
        (3, 5),    # "You win!" - 60% hit rate and hits >= spins? No, 3 < 5
        (5, 5),    # "You win!" - 100% hit rate and hits >= spins
        (6, 5),    # "You win!" - 120% hit rate and hits >= spins
    ]
    
    functions = [
        determine_progress_no_if,
        determine_progress_no_if_v2,
        determine_progress_no_if_v3
    ]
    
    print("Testing all variations:")
    for hits, spins in test_cases:
        print(f"\nTest case: hits={hits}, spins={spins}")
        results = []
        for func in functions:
            result = func(hits, spins)
            results.append(result)
            print(f"  {func.__name__}: {result}")
        
        # Check if all results are the same
        resultSet = set(results)
        length = len(resultSet)
        if length == 1:
            print(f" ✓ All versions agree")
        else:
            print(f" ✗ Versions disagree!")


if __name__ == "__main__":
    test_all_versions()


"""
ADVANTAGES AND DISADVANTAGES ANALYSIS:

ADVANTAGES of the no-if approach:
1. **Conciseness**: Once you understand the pattern, the logic is very compact
2. **Functional style**: More mathematical/functional programming approach
3. **No nested conditions**: Eliminates deeply nested if-statements
4. **Potentially faster**: Fewer branching instructions (though Python optimizes this)
5. **Table-driven**: Logic is separated from the data (messages in a list)
6. **Extensible**: Easy to add new progress levels by extending the list and conditions

DISADVANTAGES of the no-if approach:
1. **Readability**: Much harder to understand at first glance
2. **Debugging**: Difficult to step through the logic and understand what's happening
3. **Maintainability**: Hard to modify conditions without understanding the entire expression
4. **Error-prone**: Easy to get the index calculation wrong
5. **Less intuitive**: The boolean-to-integer conversion is not immediately obvious
6. **Fragile**: Small changes in conditions can break the entire index calculation
7. **Limited flexibility**: Hard to handle complex conditional logic that doesn't map to simple indices

RECOMMENDATION:
While the no-if approach is clever and demonstrates advanced Python techniques, 
the original if-statement version is generally preferable for most real-world 
applications due to its clarity and maintainability. The no-if approach is 
best used when:
- Performance is critical and you've profiled the code
- You have a clear mapping from conditions to discrete states
- The logic is unlikely to change frequently
- You're working with a team that appreciates functional programming styles
"""
