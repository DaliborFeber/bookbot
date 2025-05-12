from stats import get_word_count, get_char_count, sort_char_count
import sys

def get_book_text(filepath):
    file_content = None
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def print_report(wordCount, charCount, bookPath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordCount} total words")
    print("--------- Character Count -------")

    for charDict in charCount:
        if charDict["char"].isalpha():
            print(f"{charDict["char"]}: {charDict["num"]}")
            
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookPath = sys.argv[1]
    bookText = get_book_text(bookPath)

    print_report(get_word_count(bookText), sort_char_count(get_char_count(bookText)), bookPath)

main()