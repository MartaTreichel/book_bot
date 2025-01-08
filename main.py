path_to_file = "books/frankenstein.txt"

def words_counter(text):
    words = text.split()
    number_of_words = 0
    for _ in words:
        number_of_words += 1
    return number_of_words

def letter_counter(text):
    letters = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha() == True:
            letters[letter] = letters.get(letter, 0) +1
    # for letter, ilosc in letters.items():
    #     print(f"{letter} - {ilosc}")
    return letters

# def letter_counter(text):
#     letters = {}
#     letter = 0
#     for a in text:
#         text = text.lower()
#         if a in letters:
#             letters[a] += 1
#         else:
#             letters[a] = 1
#     return letters

#1. przeiterowac przez wszystkie litery w calym tekscie i policzyc ich wystapienia
#2. podczas petli uzyc lower
#3. sprawdz czy dany znak jest litera - .isalpha
#4. uzyj w main

def main():
    with open(path_to_file) as file:
        file_content = file.read()
        number_of_words_in_book = words_counter(file_content)
        letters = letter_counter(file_content)
    print(number_of_words_in_book)
    print(letters)



# {'p': 6121, 'r': 20818, 'o': 25225, ...
main()
