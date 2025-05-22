from stats import count_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = count_words(book_text)
    print(f"{num_words} words found in the document")

    character_counts = count_characters(book_text)
    print(character_counts)

if __name__ == "__main__":
    main()