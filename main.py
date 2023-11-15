
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    letter_count = {}

    #loop through each letter in its lower case form
    #and increment its value in the letter_count dict if the key exists
    #if not add the letter as a key to letter_count dict with value  1
    for i in range(0, len(file_contents)):
        letter = file_contents[i].lower()
        
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    character_list = list(letter_count)
    character_list.sort()
    
    letters = []
    
    for character in character_list:
        if character.isalpha():
            letters.append(character)


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words in the document")
    for letter in letters:
        print(f"The '{letter}' character was found {letter_count[letter]} times")
    print("--- End report ---")