"""
Lab Work 1: Task 4 - String Analysis
Version: 1.0
Developer: Belavusau Anton
Date: 2025-04-14
"""

def compute(s: str) -> tuple[int, tuple[str, int], str]:
    """
    Analyze a string to count lowercase letters, find the first word containing 'v', 
    and filter out words starting with 's' (case-insensitive).

    Args:
        s (str): Input string.

    Returns:
        tuple: 
            - int: Count of lowercase letters.
            - tuple: (First word with 'v', its 0-based index) or ("", -1) if not found.
            - str: String without words starting with 's'.
    """
    cnt_lower = 0
    words = []
    current_word = []
    word_with_v = ""
    word_v_index = -1
    separators = {' ', ',', '.', ';', '!', '?'}
    found_v = False

    # Process each character
    for char in s:
        if char in separators:
            if current_word:
                word = ''.join(current_word)
                words.append(word)
                # Check for 'v' in the word
                if not found_v and 'v' in word.lower():
                    word_with_v = word
                    word_v_index = len(words) - 1
                    found_v = True
                current_word = []
        else:
            current_word.append(char)
            if char.islower():
                cnt_lower += 1

    # Add the last word if any
    if current_word:
        word = ''.join(current_word)
        words.append(word)
        if not found_v and 'v' in word.lower():
            word_with_v = word
            word_v_index = len(words) - 1

    # Filter words starting with 's' (case-insensitive)
    filtered_words = [word for word in words if not word.lower().startswith('s')]
    result_str = ' '.join(filtered_words)

    return (
        cnt_lower,
        (word_with_v, word_v_index) if word_with_v else ("", -1),
        result_str
    )