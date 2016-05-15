import requests
import smtplib
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
def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/find?q=Bangalore&units=metric&appid=13093b1b0a356c3b029cce493525824d'
    weather_request = requests.get(url) #returns request object 
    weather_json = weather_request.json() #returns data in json format
    #print(weather_json)
    description = weather_json['list'][0]['weather'][0]['description']
    #print(description)
    temp_min = weather_json['list'][0]['main']['temp_min']
    #print(temp_min)
    temp_max = weather_json['list'][0]['main']['temp_max']
    #print(temp_max)

    forecast = 'Today\'s forecast is:\n ' + description + ' with a high of ' + str(temp_max) +'C  and a low of ' + str(temp_min) + 'C'
    #print(forecast)
    return forecast

def send_emails(emails,forecast):
    #1Connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com','587') # 587 is the Port for TLS/STARTTLS

    #2.Start TLS encryption
    server.starttls()

    #3.Login
    password = '11bce1792/'
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
    
    
def main():
    emails = get_emails()
    print(emails)
    
    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails,forecast)
    
main()
