# Returns the total number of words in a given text file
def get_num_words(book_text):
    return len(book_text.split())

# Returns the number of each type of character in a given text file, listed in order of appearance
def get_num_chars(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else: 
            char_count[char] = 1
    return char_count

def sort_char_counts(char_counts):
    # Create a list of dictionaries with "char" and "num" keys
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    # Sort the list by count (from greatest to least)
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def generate_report(book_path, wordcount, sorted_chars):
    lines = [
        "============ BOOKBOT ============",
        f"Analyzing book found at {book_path}...",
        "----------- Word Count ----------",
        f"Found {wordcount} total words",
        "--------- Character Count -------"
    ]
    
    # Add alphabetic character counts
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        if char.isalpha():  # Only include alphabetic characters
            lines.append(f"{char}: {count}")
    
    lines.append("============= END ===============")
    
    # Join all lines with newlines and return
    return "\n".join(lines)