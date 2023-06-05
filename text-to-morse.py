morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    ' ': '/'
}


def text_to_morse(text):
    morse = ''
    for char in text:
        if char.upper() in morse_code:
            morse += morse_code[char.upper()] + ' '
        else:
            morse += char
    return morse


def morse_to_text(morse):
    text = ''
    morse_code_reverse = {v: k for k, v in morse_code.items()}
    morse_list = morse.split(' ')
    for code in morse_list:
        if code in morse_code_reverse:
            text += morse_code_reverse[code]
        else:
            text += code
    return text


def main():
    while True:
        option = input("Enter '1' to convert text to Morse code or '2' to convert Morse code to text: ")

        if option == '1':
            text = input("Enter a string: ")
            morse = text_to_morse(text)
            print("Morse code:", morse)
        elif option == '2':
            morse = input("Enter Morse code: ")
            text = morse_to_text(morse)
            print("Text:", text)
        else:
            print("Invalid option!")

        repeat = input("Do you want to convert again? (yes/no): ")
        if repeat.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
