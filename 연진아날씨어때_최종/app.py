import requests
import json

from flask import Flask, render_template, request
app = Flask(__name__, static_url_path='/static')


@app.route('/map')
def page2():
    return render_template('test1.html')

@app.route('/')
def page1():
    return render_template('main.html')

@app.route('/weather')
def weather_get():
    city = request.args.get('city')
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

    # if 'Clear' in weather :
    #     msg = "이 맑기만 한 하늘아ㅋ"
    # elif 'Rain' in weather :
    #     msg = "우산 챙겨~ㅋ"
    # elif "Clouds" in weather :
    #     msg = "오늘부터 모든 날이 구름낄거야ㅋ"
    # elif 'Thunderstorm' in weather :
    #     msg = "너네 주님 개빡쳤어ㅋ"
    # else :
    #     msg = "날씨 봤으면 끄덕여ㅋ"

    case_fold = weather.lower()
    if 'clear' in case_fold :
        msg = "이 맑기만 한 하늘아ㅋ"
    elif 'rain' in case_fold :
        msg = "우산 챙겨~ㅋ"
    elif "clouds" in case_fold :
        msg = "오늘부터 모든 날이 구름낄거야ㅋ"
    elif 'thunderstorm' in case_fold :
        msg = "너네 주님 개빡쳤어ㅋ"
    else :
        msg = "날씨 봤으면 끄덕여ㅋ"



    # print(name)
    # print(weather)
    # print(city)
    # print(desc)
    # print(temp_max)
    # print(temp_min)
    # print(clouds)
    return render_template('test2.html', msgHtml = msg, nameHtml=name, weatherHtml=weather, descHtml=desc, temp_maxHtml = temp_max, temp_minHtml=temp_min)




# @app.route("/weather", methods=["GET"])
# def weather_get():
#     city = request.args.get('city')


if __name__ == '__main__':  
   app.run('0.0.0.0',port=8000,debug=True)
