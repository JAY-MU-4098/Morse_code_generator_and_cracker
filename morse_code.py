morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
    ')': '-.--.-', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/',
    '~': '~~', '`': '.----.', '<': '.-..-.', '>': '-.-.--', '[': '-.--.', ']': '-.--.-', '{': '.--.-.',
    '}': '.----.', '\\': '-.--.-', '|': '.-...', '*': '-.-.-', '^': '..--.-', '&': '.-...',
}

reverse_morse_code_dict = {value: key for key, value in morse_code_dict.items()}


def text_to_morse(message: str) -> str:
    """
    This function take's string and return's string in morse code.
    If character is not appropriate then will be converted to ??.
    :param message:
    :return:
    """
    morse_code = ""
    for ch in message:
        if ch in morse_code_dict:
            morse_code += morse_code_dict[ch] + ' '
        else:
            morse_code += '??'
    return morse_code


def morse_to_text(morse_cord: str) -> str:
    """
    This function take's morse code and return's text.
    If code is not appropriate then will be converted to ??
    :param morse_cord:
    :return:
    """
    message = ""
    morse_words = morse_cord.split(" ")

    for morse_word in morse_words:
        if morse_word in reverse_morse_code_dict:
            message += reverse_morse_code_dict[morse_word]
        else:
            message += '??'

    return message
