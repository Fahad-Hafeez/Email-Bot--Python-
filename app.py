import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print('listening... ')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Give app access to your Google Account
    server.login('Sender_Email', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'Fahad School': 'haf7197f@maidenerleghschools.co.uk'
}


def get_email_info():
    talk('Who do you wanna send your email to')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the the subject of your email')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Mr Lazy, Your email has been sent')
    talk('Any other emails that you wanna send')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
