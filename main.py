
def decrypt_caesar(file_name):
    """
    Takes file name of some text file that contains a message encrypted by caesars cipher. The cipher is solved by
    checking which shift contains the most occurrences of common English words. Words used from the website:
    https://www.ef.edu/english-resources/english-vocabulary/top-3000-words/. Returns shift amount as an int.
    """

    # get words from word_list.txt into some set
    word_set = set()
    with open('word_list.txt', 'r') as word_file:
        for line in word_file:
            word_set.add(line.rstrip('\n'))

    # now open the given file and count the number occurrences of words that are in word_set for every shift.
    shift_scores = {shift: 0 for shift in range(26)}

    with open(file_name, 'r') as in_file:
        text = in_file.read()

    for shift in range(26):
        shifted_word = []
        for char in text:
            # Ignore any punctuation, whitespace, etc.
            if char.isalpha():
                # modulo gets remainder after shift to help with overflow post-shift
                shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
                shifted_word.append(shifted_char)
            elif shifted_word:
                word = ''.join(shifted_word)
                if word in word_set:
                    shift_scores[shift] += 1
                shifted_word = []
        if shifted_word:
            word = ''.join(shifted_word)
            if word in word_set:
                shift_scores[shift] += 1

    best_shift = max(shift_scores, key=shift_scores.get)

    # have best shift so now write output.
    with open('output.txt', 'w') as out_file:
        for char in text:
            if char.isalpha():
                if char.islower():
                    shifted_char = chr((ord(char) - ord('a') + best_shift) % 26 + ord('a'))
                else:
                    shifted_char = chr((ord(char) - ord('A') + best_shift) % 26 + ord('A'))
                out_file.write(shifted_char)
            else:
                out_file.write(char)
    return (best_shift, shift_scores[best_shift])

def main():
    """
    Main program prompts user in console for file name then outputs the shift that was made to solve the cipher and
    where the decrypted message is.
    """
    input_file_name = input("Enter file name that has the encrypted text (empty for default): ")
    if not input_file_name:
        input_file_name = 'caesar_cipher_text.txt'
    result = decrypt_caesar(input_file_name)
    print(f'Most accurate shift amount: {result[0]}')
    print(f'Number of common words after decryption: {result[1]}')
    print('Decrypted message stored in output.txt')

if __name__ == '__main__':
    main()