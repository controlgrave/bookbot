import sys

from stats import get_num_words
from stats import get_num_chars
from stats import sort_char_counts
from stats import generate_report

def get_book_text(book):
    with open(book) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]  # This assigns just the path string
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    
    wordcount = get_num_words(text)
    char_counts = get_num_chars(text)
    sorted_chars = sort_char_counts(char_counts)
    
    report = generate_report(book_path, wordcount, sorted_chars)
    print(report)

main()