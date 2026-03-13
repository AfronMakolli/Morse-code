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
    '0': '-----', ' ': '/'
}

# Reverse dictionary for decoding
DECODE_MORSE = {v: k for k, v in MORSE_CODE.items()}

# Encode text to morse
def encode(text):
    text = text.upper()
    return ' '.join(MORSE_CODE[c] for c in text if c in MORSE_CODE)

# Decode morse to text
def decode(morse):
    words = morse.split(' ')
    return ''.join(DECODE_MORSE[w] if w in DECODE_MORSE else '' for w in words)

# Play morse using beep
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

# ---- MAIN LOOP ----
while True:
    text = input("Shkruaj tekstin (ose shkruaj 'exit' per me dal): ")
    if text.lower() == 'exit':
        break

    morse = encode(text)
    print("Morse Code:", morse)

    play_morse(morse)

    decoded = decode(morse)
    print("Decoded:", decoded)
    print("\n---\n")