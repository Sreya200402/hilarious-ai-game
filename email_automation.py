import random
from email.message import EmailMessage
import smtplib

def otp_gen():
    otp = random.randint(1000, 9999)
    return otp


def email_create_send(otp, s_email_id, s_password, r_email):
    mail = EmailMessage()
    mail['To'] = r_email
    mail['Subject'] = "OTP for verification"
    body = f"Your OTP for verification is {otp}.Please use this to verify your email."
    mail.set_content(body)
    
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.starttls()
    server.login(s_email_id, s_password)
    server.send_message(mail)
    server.quit()

    print("OTP sent")

def otp_verify(otp):
    uotp = int(input('Enter the OTP you received:'))
    if otp == uotp:
        print('Verification successful!!!')
    else:
        print('Verification failed!!!')

otp = otp_gen()
receiver = input('enter the mail of receiver:')
s_email_id = 'pasalasreyagracy@gmail.com'
s_password = 'dqhb aapu aluz jmjk'
email_create_send(otp,s_email_id,s_password,receiver)
otp_verify(otp)