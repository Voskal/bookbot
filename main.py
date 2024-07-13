def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_no = count_words(text)
    print(text)
    print(f"This book has {word_no} words." )

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

main()