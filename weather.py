import requests
from bs4 import BeautifulSoup
import json
from urllib.request import urlopen
import schedule 
import time

def live_location(url):
    response=urlopen(url)#To open the location url
    data=json.load(response)
    global loc
    loc=data['region'] #returns the current location

    
url='https://ipinfo.io/json'
live_location(url)
def weather_info(url):
    resp=requests.get(url)
    #srapping the weather information from web
    soup=BeautifulSoup(resp.text,"lxml")
    temp=soup.find("div",class_="BNeawe iBp4i AP7Wnd").text
    pres=soup.find("div",class_="BNeawe tAd8D AP7Wnd").text.split()
    global info
    info=(f"{temp} {pres[-1]}") #returns the weather 
url=f"https://www.google.com/search?q=weather+{loc}"
weather_info(url) 

 
def schedule_notify(): 
    global a
    a=toast.show_toast(f"TODAY'S WEATHER IN {str(loc).upper()}",info,duration=5)
    print(a)
toast=ToastNotifier()
 #schedule for desktop niotification at every day 9AM    
schedule.every().day.at("09:00").do(schedule_notify)
while True:
    schedule.run_pending()
    
