import requests
import json

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def page2():
    return render_template('test1.html')

@app.route('/weather')
def weather_get():
    city = request.form['cityTitle']
    apiKey = "1f9654032dcb7c4cf2bfd1c49c8a05d1"
    lang = 'kr' #언어
    units = 'metric' #화씨 온도를 섭씨 온도로 변경
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units={units}"

    result = requests.get(api)
    result = json.loads(result.text)

    name = result['name']
    weather = result['weather'][0]['main']
    desc = result['weather'][0]['description']
    temp_max = result['main']['temp_max']
    temp_min = result['main']['temp_min']
    clouds = result['clouds']['all']

    # print(name)
    # print(weather)
    # print(desc)
    # print(temp_max)
    # print(temp_min)
    # print(clouds)
    return render_template('index.html', nameHtml=name, weatherHtml=weather, descHtml=desc, temp_maxHtml = temp_max, temp_minHtml=temp_min, cloudsHtml=clouds)




# @app.route("/weather", methods=["GET"])
# def weather_get():
#     weather_data = 


if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)
