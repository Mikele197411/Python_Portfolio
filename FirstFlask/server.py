from flask import Flask
from weather import get_weather
from datetime import datetime
app= Flask(__name__)
@app.route('/')
def index():
    data="https://api.openweathermap.org/data/2.5/weather?q=London,uk&units=metric&APPID=91743a0135ee6679819c9aecbbee8922"
    weather=get_weather(data)
    cur_date=datetime.now().strftime('%d.%m.%Y',)
    result='<p>Temp: %s</p>' % weather['main']['temp']
    result+='<p>City: %s</p>' % weather['coord']
    result+='<p>Date: %s</p>' % cur_date
    return result
   

app.run() 
