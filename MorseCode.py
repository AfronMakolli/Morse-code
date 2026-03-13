import winsound
import time

# Morse Code dictionary
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...',
    'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',
    ' ': '/'
}

# Reverse dictionary
DECODE_MORSE = {v: k for k, v in MORSE_CODE.items()}


# Encode text to Morse
def encode(text):
    text = text.upper()
    return ' '.join(MORSE_CODE[c] for c in text if c in MORSE_CODE)


# Decode Morse to text
def decode(morse):
    words = morse.split(' ')
    decoded_text = ""

    for w in words:
        if w == '/':
            decoded_text += " "
        elif w in DECODE_MORSE:
            decoded_text += DECODE_MORSE[w]
        else:
            decoded_text += '?'

    return decoded_text


# Play Morse sound
def play_morse(morse):
    frequency = 800
    dot_duration = 150
    dash_duration = 450

    for symbol in morse:
        if symbol == '.':
            winsound.Beep(frequency, dot_duration)
        elif symbol == '-':
            winsound.Beep(frequency, dash_duration)
        elif symbol == ' ':
            time.sleep(0.2)
        elif symbol == '/':
            time.sleep(0.6)


# ---- MAIN PROGRAM ----
choice = input("Shkruaj 'enkriptim' ose 'dekriptim': ")

if choice.lower() == "enkriptim":

    while True:
        text = input("Shkruaj tekstin (ose 'exit' për me dal): ")

        if text.lower() == "exit":
            break

        morse = encode(text)
        print("Morse Code:", morse)

        play_morse(morse)

        decoded = decode(morse)
        print("Decoded:", decoded)
        print("\n---\n")

elif choice.lower() == "dekriptim":

    while True:
        morse_input = input("Shkruaj Morse code (ose 'exit' për me dal): ")

        if morse_input.lower() == "exit":
            break

        print("Luaj Morse me beep:", morse_input)
        play_morse(morse_input)

        decoded = decode(morse_input)
        print("Dekodu:", decoded)
        print("\n---\n")

else:
    print("Opsion i pavlefshëm.")