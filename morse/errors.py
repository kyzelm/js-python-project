class WrongMorseCodeError(Exception):
    def __init__(self, message="Invalid Morse code input."):
        self.message = message
        super().__init__(self.message)

class MorseCodeNotFoundError(Exception):
    def __init__(self, char, message="Morse code not found for character."):
        self.char = char
        self.message = f"{message} '{char}'"
        super().__init__(self.message)