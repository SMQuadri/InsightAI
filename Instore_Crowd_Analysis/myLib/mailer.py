import smtplib, ssl

class Mailer:
    
    def __init__(self):
        
        # Enter your email below. This email will be used to send alerts.
        # Eg: "email@gmail.com"
        self.EMAIL = ""
        
        # Enter the email password below. Note that the corresponding mail id you entered above must be a 2 step verified google account.
        # Only then you could generate the corresponding 16 character app key password which you.
        # Paste your generated 16 character password below.
        # Eg: "cjudtykamnxdqiow"
        # To create 2 step verification and then turn it on. You can refer the links below and create an application specific password.
        # Google mail has a guide here: https://myaccount.google.com/lesssecureapps
        # For 2 step verified accounts: https://support.google.com/accounts/answer/185833
        self.PASS = ""
        
        self.PORT = 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)

    def send(self, mail):
        
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', self.PORT)
        self.server.login(self.EMAIL, self.PASS)
        
        SUBJECT = 'ALERT'
        TEXT = f'ALERT - This mail is to hereby inform you that the maximum limit for people violating social distancing in your store has been exceeded !'
        message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

        self.server.sendmail(self.EMAIL, mail, message)
        self.server.quit()
