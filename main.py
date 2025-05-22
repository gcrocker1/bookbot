def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    num_words = len(text.split())
    return num_words


def main():
    num_words = count_words(get_book_text('books/frankenstein.txt'))
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()