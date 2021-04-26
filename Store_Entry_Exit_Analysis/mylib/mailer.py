import smtplib, ssl

class Mailer:
    
    def __init__(self):
        
        self.EMAIL = "smquadri1999@gmail.com"
        self.PASS = "cfytwtrlixiipwrn"
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        
        SUBJECT = 'ALERT'
        TEXT = f'This mail is to hereby inform you that the maximum limit for people in your store has been exceeded !'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()