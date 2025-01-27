def main():
    with open('books/frankenstein.txt') as file:
        text = file.read()

    total_words = count_words(text)
    char_dict = count_occurences(text)
    sorted_dict = sort_dict(char_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f'{total_words} words found in the document\n')
    for k,v in sorted_dict:
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")
    print("--- End of report ---")

def sort_dict(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)


def count_words(text):
    return len(text.split())


def count_occurences(text):
    lowered_string = text.lower()
    dictionary = {" ": 0}
    for char in lowered_string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

main()
