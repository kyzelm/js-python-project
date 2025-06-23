from .utils import morseCode, words, sentences
from .coders import Decoder, Encoder
from .fileManager import FileManager
import random as rand


class MorseLearning:
    def __init__(self):
        self.level = 1
        self.toLearn = []
        self.encoder = Encoder()
        self.decoder = Decoder()
        self.fileManager = FileManager('morseData.json')

    def readFile(self):
        data = self.fileManager.read_JSON_file()
        if data:
            self.level = data.get('level', 1)
            self.toLearn = data.get('toLearn', [])
        else:
            print("No data found in the file. Starting fresh.")

    def writeFile(self):
        data = {
            'level': self.level,
            'toLearn': self.toLearn
        }
        self.fileManager.write_JSON_file(data)

    def setup(self):
        self.readFile()
        if not self.toLearn:
            if self.level == 1 or self.level == 2:
                for letter in morseCode.keys():
                    self.toLearn.append(letter)
            elif self.level == 3 or self.level == 4:
                self.toLearn = list(words)
            elif self.level == 5 or self.level == 6:
                self.toLearn = list(sentences)

    def learn(self):
        self.setup()

        while self.toLearn:
            item = rand.choice(self.toLearn)

            if self.level % 2 == 1:
                print(f"Translate to Morse Code:\n{item}")
                answer = input("Your answer: ").strip().upper()
                if answer == self.encoder.action(item):
                    print("Correct!")
                    tmpList = filter(lambda letter: letter != item, self.toLearn)
                    self.toLearn = list(tmpList)
                    self.writeFile()
                elif answer == "EXIT":
                    print("Exiting the learning session.")
                    break
                else :
                    print(f"Incorrect! The correct answer is:\n{self.encoder.action(item)}")
            else:
                print(f"Translate from Morse Code:\n{self.encoder.action(item)}")
                answer = input("Your answer: ").strip().upper()
                if answer == item:
                    print("Correct!")
                    self.toLearn.remove(item)
                    self.writeFile()
                elif answer == "EXIT":
                    print("Exiting the learning session.")
                    break
                else:
                    print(f"Incorrect! The correct answer is:\n{item}")

        if not self.toLearn:
            if self.level < 6:
                self.level += 1
                print(f"Level up! Now you are at level {self.level}.")
                self.writeFile()
            else:
                self.level = 1
                print("Congratulations! You have mastered all levels of Morse Code learning.")
                self.writeFile()