from gtts import gTTS
import os
import sys

def text_to_speech(text, lang='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

    # Check the operating system and open the audio file accordingly
    if os.name == 'nt':  # For Windows
        os.system("start " + filename)
    elif os.name == 'posix':  # For Linux and macOS
        if sys.platform.startswith('darwin'):  # macOS
            os.system("afplay " + filename)
        elif 'linux' in sys.platform:  # Linux
            os.system("xdg-open " + filename)
        else:
            print("Unsupported operating system")
    else:
        print("Unsupported operating system")

# Example usage:
text = "Hello, how are you?, if you are fine then I am also fine and please give one star if you like this project"
text_to_speech(text)
