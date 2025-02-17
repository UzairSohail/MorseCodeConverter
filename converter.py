MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}

def morse_to_text(morse:str):
    """Translates morse code into readable string format"""
    morse_words = morse.split(sep="/")
    morse_letters = [words.strip().split(" ") for words in morse_words]
    result=""
    for word in morse_letters:
        for letter in word:
            if letter!="":
                try:
                    val =next(key for key,value in MORSE_CODE_DICT.items() if MORSE_CODE_DICT[key] == letter)
                    result+=(val.strip())
                except StopIteration:
                    print('not found')
        result+=" "
    return result

def text_to_morse(text:str):
    """Takes a string and returns the morse code equivalent"""
    text = text.split(sep=" ")
    result=""
    for i in text:
        for chars in i.upper():
            result += MORSE_CODE_DICT[chars]+" "
        result+="/"
    return result