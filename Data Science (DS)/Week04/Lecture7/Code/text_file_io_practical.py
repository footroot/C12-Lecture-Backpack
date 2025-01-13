"""
Word Counter with Stop Words Removal
----------------------------------

Problem Description:
This program counts how many times each word appears in a text file while ignoring common words
(like "the", "a", "is") called stop words. It follows these steps:
1. Reads text from an input file
2. Cleans the text (removes punctuation, converts to lowercase)
3. Removes common words (stop words) that don't add meaning
4. Counts how many times each remaining word appears
5. Saves the results to an output file

Required files:
- input.txt: The text file you want to analyze
- stop_words.txt: A file containing common words to ignore (one word per line)
- output.txt: Where the results will be saved (created automatically)

Example:
If input.txt contains: "The quick brown fox jumps over the lazy dog"
And stop_words.txt contains: "the over"
The program will count: "quick", "brown", "fox", "jumps", "lazy", "dog"
"""

def read_file(file_path): 
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path to the file you want to read
    
    Returns:
        str or None: The content of the file, or None if the file doesn't exist
        None: If the file does not exist.
    """
    try: 
        with open(file_path, 'r') as file: 
            content = file.read() 
        return content 
    except FileNotFoundError: 
        print("Error: The file does not exist.") 
        return None 

def preprocess_text(text): 
    """
    Cleans the text by removing punctuation and converting it to lowercase.

    This function takes a string (`text`) and performs two cleaning steps:

    1. Lowercase conversion: Converts all characters to lowercase using `text.lower()`.
    2. Punctuation removal: Removes all punctuation characters using a loop and string manipulation.

    For example:
    "Hello, World!" becomes "hello world"
    
    Args:
        text (str): The text to clean
    
    Returns:
        str: The cleaned text
    """
    import string 
    # Convert everything to lowercase
    text = text.lower() 
    # Remove all punctuation marks (.,!? etc.)
    for char in string.punctuation: 
        text = text.replace(char, "") 
    return text 

def remove_stopwords(words, stopwords): 
    """
    Removes common words (stop words) from a list of words.
    
    Args:
        words (list): List of words to filter
        stopwords (list): List of common words to remove
    
    Returns:
        list: Words with stop words removed
    
    Example:
        words = ['the', 'quick', 'fox']
        stopwords = ['the']
        Returns: ['quick', 'fox']
    """
    return [word for word in words if word not in stopwords] 

def count_words(words): 
    """
    Counts how many times each word appears in the list.
    
    Args:
        words (list): List of words to count
    
    Returns:
        dict: Dictionary where keys are words and values are their counts
    
    Example:
        ['fox', 'quick', 'fox'] becomes {'fox': 2, 'quick': 1}
    """
    word_count = {} 
    # Count each word
    for word in words: 
        if word in word_count:  # If we've seen this word before
            word_count[word] += 1  # Increase its count
        else:  # If this is a new word
            word_count[word] = 1  # Start counting from 1
    return word_count 

def write_word_counts(word_counts, output_file): 
    """
    Saves the word counts to a file.
    
    Args:
        word_counts (dict): Dictionary of words and their counts
        output_file (str): Name of the file to save results
    """
    # Open file in write mode ('w')
    with open(output_file, 'w') as file: 
        # Write each word and its count on a new line
        for word, count in word_counts.items(): 
            file.write(f"{word}: {count}\n") 
    print(f"Word counts written to {output_file}") 

def load_stop_words(file_path="stop_words.txt"): 
    """
    Reads common words to ignore from a file.
    
    Args:
        file_path (str): Path to the file containing stop words
    
    Returns:
        list: List of stop words, or empty list if file doesn't exist
    """
    stopwords = [] 
    try: 
        # Read the file line by line
        with open(file_path, 'r') as file: 
            for line in file: 
                stopwords.append(line.strip())  # Remove whitespace and add to list
        return stopwords 
    except FileNotFoundError: 
        print("Error: The file does not exist.") 
        return stopwords  # Return empty list if file not found

def main(): 
    """
    Main function that runs the word counting program.
    """
    # Load the list of words to ignore
    stopwords = load_stop_words()
    
    # File names
    input_file = "input.txt"  # The file to analyze
    output_file = "output.txt"  # Where to save the results

    # Step 1: Read the input file
    text = read_file(input_file) 
    if text is None:  # If we couldn't read the file
        return  # Stop the program

    # Step 2: Clean the text
    text = preprocess_text(text) 

    # Step 3: Split text into individual words
    words = text.split() 

    # Step 4: Remove common words
    filtered_words = remove_stopwords(words, stopwords) 

    # Step 5: Count how many times each word appears
    word_counts = count_words(filtered_words) 

    # Step 6: Save the results
    write_word_counts(word_counts, output_file) 

# Run the main function
main()