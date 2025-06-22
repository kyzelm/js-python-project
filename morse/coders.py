from .morseCode import morseCode
from .errors import WrongMorseCodeError, MorseCodeNotFoundError

class Coder:
    def action(self, text):
        raise NotImplementedError("Subclasses should implement this method.")

class Encoder(Coder):
    def action(self, text):
        encoded_text = []
        for char in text:
            try:
                if char.upper() in morseCode:
                    encoded_text.append(morseCode[char.upper()])
                else:
                    raise MorseCodeNotFoundError(char)
            except MorseCodeNotFoundError as e:
                print(e.message)
        return ' '.join(encoded_text)

class Decoder(Coder):
    def action(self, morse_code):
        decoded_text = []
        morse_words = morse_code.split(' ')
        for code in morse_words:
            try:
                if code in morseCode.values():
                    decoded_text.append(list(morseCode.keys())[list(morseCode.values()).index(code)])
                else:
                    raise WrongMorseCodeError()
            except WrongMorseCodeError as e:
                print(e.message)
        return ''.join(decoded_text)