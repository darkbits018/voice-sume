import pyttsx3
import speech_recognition as sr


# Initialize text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


# Get audio input from the user
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=20)
            print("Processing...")
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Error in speech recognition service."
        except Exception as e:
            return f"An error occurred: {e}"


# Ask a single question and get the response
def single_question_qa():
    question = "What is your name?"
    print(f"AI: {question}")
    speak(question)
    response = listen()
    print(f"User's Response: {response}")


if __name__ == "__main__":
    single_question_qa()
