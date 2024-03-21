def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()

    selected_words = {}

    for line in lines:
        num, words = line.split(maxsplit=1)
        if ((8 * int(num) + 1)**0.5).is_integer() and ((8 * int(num) + 1)**0.5)>0:
            selected_words[int(num)] = words.rstrip('\n')

    counter = 3
    decoded_words = selected_words[1]
    for i in range(1, len(selected_words)):
        decoded_words = decoded_words + ' ' + selected_words[counter]
        counter+=(i+2)

    print('m' + decoded_words + 'k')
    return decoded_words

# Example usage
message_file = "coding_qual_input.txt"  # Replace with the actual path to your file
decoded_message = decode(message_file)
#print(decoded_message)