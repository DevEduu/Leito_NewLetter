import imaplib
import quopri
from os import getenv

import pyttsx3
from bs4 import BeautifulSoup
from dotenv import load_dotenv


class Read_new_latter:
    def __init__(self):
        self.FROM_EMAIL = getenv('EMAIL')
        self.FROM_PWD = getenv('TOKEN_PASS')
        self.SMTP_SERVER = 'imap.gmail.com'
        self.SMTP_PORT = getenv('SMTP_PORT')

    def main(self):
        self.read_voice()

    def Open_config_server(self):
        """Open config server gmails."""
        mail = imaplib.IMAP4_SSL(self.SMTP_SERVER, self.SMTP_PORT)
        mail.login(self.FROM_EMAIL, self.FROM_PWD)
        mail.select('Deschamps')   # Name for Fold tag
        status, data = mail.search(None, '(UNSEEN)')   # ALL / UNSEEN
        return data

    def filter_read_email(self):
        data = self.Open_config_server()
        for num in data[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            EMAIL_MSG = data[0][1]

            soup = BeautifulSoup(markup=EMAIL_MSG, features='html.parser')
            news = soup.find_all('td')[0].text

            utf = quopri.decodestring(news)
            text_formated = utf.decode('utf-8')

            return text_formated

    def read_voice(self):
        text = self.filter_read_email()
        engine = pyttsx3.init()
        engine.say('Bom dia Mestre!')
        engine.say(text)
        engine.runAndWait()


if __name__ == '__main__':
    read_new = Read_new_latter()
    read_new.main()
