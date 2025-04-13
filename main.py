import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

r = sr.Recognizer()
engine = pyttsx3.init()

# Initialize Gemini
genai.configure(api_key="AIzaSyDr49uAU13FwTyaJInQ5JZlVKX1ZupC9tA")  # Replace with your API key
model = genai.GenerativeModel("gemini-2.0-flash")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error using Gemini: {e}"


def process_command(command):
        response = ask_gemini(command)
        print("Gemini:", response)
        speak(response)
        
if __name__ == "__main__":
    speak("Initializing voice assistant...")
    while True:
        try:
            # Listen for commands
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            # Recognize speech 
                command = r.recognize_google(audio)
                if command.lower() == "jarvis":
                    speak("Hello, how can I assist you?")
                    print("Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"You said: {command}")
                    process_command(command)
                

        except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                speak("Sorry, I did not understand that.")