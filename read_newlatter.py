import imaplib
from bs4 import BeautifulSoup
import quopri
import pyttsx3

def LeitorNewLatter():
    FROM_EMAIL = "seu email"
    FROM_PWD = "sua senha"
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993

    #Abrindo coneção
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select("Deschamps")
    status, data = mail.search( None, "(UNSEEN)") # ALL / UNSEEN

    for num in data[0].split():
        status, data = mail.fetch(num, "(RFC822)")
        EMAIL_MSG = data[0][1]

        soup = BeautifulSoup(markup=EMAIL_MSG, features="html.parser")
        news = soup.find_all("td")[0].text

        utf = quopri.decodestring(news)
        text = utf.decode('utf-8')

        engine = pyttsx3.init()
        engine.say("Bom dia Mestre!")
        engine.say(text)
        engine.runAndWait()

LeitorNewLatter()
