import sys
from stats import count_words, count_characters, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:   # if path to file is not provided, prompt the user to do so
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file = sys.argv[1]     # Using system arguments to get path to file from user input on CLI
    book_text = get_book_text(book_file)
    num_words = count_words(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    character_counts = count_characters(book_text)
    #print(character_counts)
    sorted_chars = sort_dict(character_counts)
    for char_count in sorted_chars:
        if char_count['char'].isalpha():
            print(f"{char_count['char']}: {char_count['num']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()