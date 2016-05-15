import smtplib

def send_emails(emails,forecast):
    #1Connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com','587') # 587 is the Port for TLS/STARTTLS

    #2.Start TLS encryption
    server.starttls()

    #3.Login
    password = '***********'
    email_from = 'ranishroy8@gmail.com'
    server.login(email_from,password)

    #4.Send mail
    for to_email,name in emails.items(): #emails.items() coz its a list
        message = 'Subject: Weather forecast\n'
        message += 'Hi ' + name +'!!\n\n'
        message += forecast
        server.sendmail(email_from, to_email, message )

    #5.Disconnect
    server.quit()
