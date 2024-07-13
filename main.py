def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_no = count_words(text)
    char_no = count_chars(text)
    print(text)
    print(f"This book has {word_no} words." )
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    words = book.split()
    char_count = {}
    for char in words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
main()