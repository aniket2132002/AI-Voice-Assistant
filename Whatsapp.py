import pywhatkit as kit
import pyttsx3

# Initialize the voice engine for feedback
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def send_whatsapp_message(message):
    number = "+919370828880"  # phone number with country code
    try:
        # Use pywhatkit to send a message instantly
        kit.sendwhatmsg_instantly(number, message)
        speak("Message sent successfully")
    except Exception as e:
        speak("An error occurred while sending the message")
        print(e)
