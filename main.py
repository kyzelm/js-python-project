from morse import Encoder, Decoder, MorseLearning

def main():
    while True:
        print("Choose an option:")
        print("1. Learn Morse Code")
        print("2. Encoder")
        print("3. Decoder")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Starting Morse Code learning...")
            learning = MorseLearning()
            learning.learn()
        elif choice == '2':
            print("Enter text to encode into Morse code:")
            text = input()
            encoder = Encoder()
            encoded_text = encoder.action(text)
            print(f"Encoded Morse Code: {encoded_text}")
        elif choice == '3':
            print("Enter Morse code to decode (separate letters with spaces):")
            morse_code = input()
            decoder = Decoder()
            decoded_text = decoder.action(morse_code)
            print(f"Decoded Text: {decoded_text}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()