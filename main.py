from collections import Counter

path_to_file = "books/frankenstein.txt"

def words_counter(text):
    words = text.split()
    number_of_words = 0
    for _ in words:
        number_of_words += 1
    return number_of_words

def letter_counter(text):
    return Counter(letter for letter in text.lower() if letter.isalpha())

def main():
    with open(path_to_file) as file:
        file_content = file.read()
        number_of_words_in_book = words_counter(file_content)
        number_of_letters_in_book = letter_counter(file_content)
        print(f"--Begin report of {path_to_file} ---")
        print(f"{number_of_words_in_book} words found in the document")
        print()
        for letter, count in number_of_letters_in_book.items():
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")


main()
