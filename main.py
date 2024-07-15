def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_no = count_words(text)
    char_no = count_chars(text)
    sorted_filtered = sort_and_filter(char_no)
    print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"This book has {word_no} words.\n" )
    for key in sorted_filtered:
        print(f"The '{key}' character was found {sorted_filtered[key]} times")
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    return len(words)

def count_chars(book):
    words = book.split()
    words = [x.lower() for x in words]
    char_count = {}
    for ele in words:
        for char in ele:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
    return char_count

def sort_and_filter(input_dict):
    letters_only = {}
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        if key.isalpha():
            letters_only[key] = value
    return letters_only


main()