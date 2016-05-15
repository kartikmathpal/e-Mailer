import weather
import mailer



def get_emails():
    emails = {} #create an empty dictionary

    try:
        email_file = open('emails.txt', 'r')    
        for line in email_file:
            (email,name) = line.split(',') #tuple  
            emails[email]  = name.strip()  #setting key,value  and clearing white space
    except FileNotFoundError as err:
        print(err)
    
    return emails
    
    
def main():
    emails = get_emails()
    print(emails)
    
    forecast = weather.get_weather_forecast()
    print(forecast)

    mailer.send_emails(emails,forecast)
    
main()
