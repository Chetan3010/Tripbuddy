# import smtplib
# import ssl
# from email.message import EmailMessage

# email_sender = 'tripbuddy.in@gmail.com'
# email_password = 'pxrwozlyauqvzlxj'
# email_receiver = 'ckale6795@gmail.com'

# subject = 'Check out my new video!'
# body = """
# I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg
# """

# em = EmailMessage()
# em['From'] = email_sender
# em['To'] = email_receiver
# em['Subject'] = subject
# em.set_content(body)

# context = ssl.create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())

import math, random
 
# def generateOTP() :
 
#     digits = "0123456789"
#     OTP = ""

#     for i in range(4) :
#         OTP += digits[math.floor(random.random() * 10)]
 
#     return OTP

# otp = generateOTP()
# print(type(otp))
# print("OTP of 4 digits:", otp)

otp = 0
for i in range(4):
    dig = math.floor(random.random() * 10)
    otp = (otp * 10) + dig

print(type(otp))
