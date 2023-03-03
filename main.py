with open('books/frankestein.txt') as f:
    file_contents = f.read()
    words_arr = file_contents.split()
    word_dict = {}
    for word in words_arr:
        for letter in word.lower():
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
    for character in word_dict:
        freq = word_dict[character]
        print(f"The \"{character}\" character was found {freq} times")
