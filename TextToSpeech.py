# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

# DATA STRUCTURES AND ALGORITHMS
# SEATWORK
# PROGRAMMED BY: Nikka Pauline D. Generalao
# BSCOE 2-2

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

import pyttsx3

def main():
    class TextToSpeech:
        engine: pyttsx3.Engine

        def __init__(self, voice, rate:int, volume: float):
            self.engine = pyttsx3.init()
            if voice:
                self.engine.setProperty('voice', voice)
            self.engine.setProperty('rate', rate)
            self.engine.setProperty('volume', volume)

        def list_available_voices(self):
            voices: list = [self.engine.getProperty('voices')]

            for i, voice in enumerate(voices[0]):
                print(f'{i + 1} {voice.name} {voice.age}: {voice.languages[0]} ({voice.gender}) [{voice.id}]')

        def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
            self.engine.say(text)
            print("\nI am speaking..")

            if save:
                self.engine.save_to_file(text, file_name)

            self.engine.runAndWait()

    if __name__=='__main__':
        text = input("\nEnter text: ")
        texttospeech = TextToSpeech(None, 200, 1.0)
        # texttospeech.list_available_voices()
        texttospeech.text_to_speech(text)

while True:
    main()

    try_again = input("\nDo you want to try again? (y/n): ")
    if try_again == "y":
        continue
    elif try_again == "n":
        print("\nThank you for using this program!! <3")
        break
    else:
        print("\nPlease enter a valid answer.")
        break

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-