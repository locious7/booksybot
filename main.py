def main() -> None:
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    count_of_words = count_words(book_text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Number of words in the file: {count_of_words}\n")

    char_count = character_count(book_text)
    for key, value in sorted(char_count.items()):
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    
    print("--- End report ---")


def read_book(book_path) -> str:
    with open(file=(book_path)) as file:
        file_contents = file.read()
        # print(file_contents)
        return file_contents

def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def character_count(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            # print(char)
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


if __name__ == "__main__":
    main()