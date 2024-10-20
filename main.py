
def decrypt_caesar(file_name):
    """
    Takes file name of some text file that contains a message encrypted by caesars cipher. The cipher is solved by
    checking which shift contains the most occurrences of common English words. Words used from the website:
    https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/. Returns shift amount as an int.
    """

    # get words from word_list.txt into some set
    word_set = set()
    with open('word_list.txt', 'r') as file:
        for line in file:
            word_set.add(line.rstrip('\n'))

    # now open the given file and count the number occurrences of words that are in word_set for every shift.
    max_words = 0
    best_shift = 0

    for i in range(1, 26):
        pass

def main():
    """
    Main program prompts user in console for file name then outputs the shift that was made to solve the cipher and
    where the decrypted message is.
    """
    decrypt_caesar('')
    pass

if __name__ == '__main__':
    main()