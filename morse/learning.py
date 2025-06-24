from .utils import morseCode, words, sentences
from .coders import Decoder, Encoder
from .fileManager import FileManager
import random as rand
import time
import matplotlib.pyplot as plt

class MorseLearning:
    def __init__(self):
        self.level = 1
        self.toLearn = []
        self.levelTime = []
        self.encoder = Encoder()
        self.decoder = Decoder()
        self.fileManager = FileManager('morseData.json')

    def readFile(self):
        data = self.fileManager.read_JSON_file()
        if data:
            self.level = data.get('level', 1)
            self.toLearn = data.get('toLearn', [])
            self.levelTime = data.get('levelTime', [])
        else:
            print("No data found in the file. Starting fresh.")

    def writeFile(self):
        data = {
            'level': self.level,
            'toLearn': self.toLearn,
            'levelTime': self.levelTime
        }
        self.fileManager.write_JSON_file(data)

    def setup(self):
        self.readFile()
        if not self.toLearn:
            if self.level == 1 or self.level == 2:
                for letter in morseCode.keys():
                    self.toLearn.append(letter)
                    self.toLearn.append(letter)
                    self.toLearn.append(letter)
            elif self.level == 3 or self.level == 4:
                self.toLearn = list(words) + list(words) + list(words)
            elif self.level == 5 or self.level == 6:
                self.toLearn = list(sentences) + list(sentences) + list(sentences)
            if self.level == 1:
                self.levelTime = [0, 0, 0, 0, 0, 0]

    def learn(self):
        self.setup()

        while self.toLearn:
            item = rand.choice(self.toLearn)
            currTime = time.time()

            if self.level % 2 == 1:
                print(f"Translate to Morse Code:\n{item}")
                answer = input("Your answer: ").strip().upper()
                if answer == self.encoder.action(item):
                    print("Correct!")
                    self.toLearn.remove(item)
                    tmpListCount = len(list(filter(lambda letter: letter == item, self.toLearn)))
                    if tmpListCount == 0:
                        print("Great job! You have learned this item completely.")
                elif answer == "EXIT":
                    print("Exiting the learning session.")
                    break
                else:
                    print(f"Incorrect! The correct answer is:\n{self.encoder.action(item)}")
            else:
                print(f"Translate from Morse Code:\n{self.encoder.action(item)}")
                answer = input("Your answer: ").strip().upper()
                if answer == item:
                    print("Correct!")
                    self.toLearn.remove(item)
                    tmpListCount = len(list(filter(lambda letter: letter == item, self.toLearn)))
                    if tmpListCount == 0:
                        print("Great job! You have learned this item completely.")
                elif answer == "EXIT":
                    print("Exiting the learning session.")
                    break
                else:
                    print(f"Incorrect! The correct answer is:\n{item}")
            elapsedTime = time.time() - currTime
            self.levelTime[self.level - 1] += elapsedTime
            self.writeFile()

        if not self.toLearn:
            if self.level < 6:
                self.level += 1
                print(f"Level up! Now you are at level {self.level}.")
                self.writeFile()
            else:
                self.level = 1
                print("Congratulations! You have mastered all levels of Morse Code learning.")
                plt.plot(range(1, 7), self.levelTime)
                plt.xlabel('Level')
                plt.ylabel('Time (seconds)')
                plt.title('Time Spent Learning Morse Code by Level')
                plt.savefig('morse_learning_time.png')
                plt.show()
                self.writeFile()