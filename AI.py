import os
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr

# Use environment variables for sensitive data
openai.api_key = os.getenv('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')
lang = 'en'

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=30)
            said = r.recognize_google(audio)
            print("You said:", said)
            return said.lower()
        except sr.WaitTimeoutError:
            print("Listening timeout.")
            return ""

def main():
    print("Starting J. A. R. V. I. S.")

    while True:
        user_input = get_audio()

        if "Jarvis" in user_input:
            try:
                completion = openai.Completion.create(
                    engine="gpt-3.5-turbo",
                    prompt=user_input,
                    max_tokens=50
                )
                response_text = completion.choices[0].text
                tts = gTTS(text=response_text, lang=lang, slow=False)
                tts.save("response.mp3")
                print(response_text)
                playsound.playsound("response.mp3")
            except Exception as e:
                print("Error:", e)

        if "Jarvis stop" in user_input:
            print("Kitsune stopping...")
            break

if __name__ == "__main__":
    main()