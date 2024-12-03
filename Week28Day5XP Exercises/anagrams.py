from anagram_checker import AnagramChecker

def is_valid_input(word):
    return word.isalpha() and len(word.split()) == 1

def main():
    checker = AnagramChecker('word_list.txt')

    while True:
        choice = input("\nMenu:\n1. Input a word\n2. Exit\nChoose an option (1 or 2): ")
        if choice == '1':
            user_input = input("Enter a word: ").strip()
            if not is_valid_input(user_input):
                print("Error: Please enter a single valid word containing only alphabetic characters.")
                continue

            valid = checker.is_valid_word(user_input)
            anagrams = checker.get_anagrams(user_input)
            print(f"\nYOUR WORD: \"{user_input.upper()}\"")
            print("This is a valid English word." if valid else "This is not a valid English word.")
            print(f"Anagrams for your word: {', '.join(anagrams) if anagrams else 'No anagrams found.'}.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()