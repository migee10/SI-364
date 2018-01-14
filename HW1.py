## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments, the people you worked with on this assignment AND any resources you used to find code (50 point deduction for not doing so). If none, write "None".
## Michele Gee

##
import requests
import json
from datetime import datetime as dt

## [PROBLEM 1] - 150 points
## Below is code for one of the simplest possible Flask applications. Edit the code so that once you run this application locally and go to the URL 'http://localhost:5000/class', you see a page that says "Welcome to SI 364!"

from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'

@app.route('/class')
def lass():
    return 'Welcome to SI 364!'





## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big
#dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like
#the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go
#to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl'
#for example, you should see data on the page that looks like this:

@app.route('/movie/<name>')
def mov(name):
    url = "http://itunes.apple.com/search"
    params = {"media": "movie", "term": name}
    get_name = requests.get(url, params = params)
    json_format = json.loads(get_name.text)
    return get_name.text

# {
#  "resultCount":0,
#  "results": []
# }


## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.

@app.route('/question', methods = ['POST', 'GET'])
def favorite():
    i = """<DOCTYPE html>
<html>
<body>
<form action = "/result" method = "GET">
<div>
    Enter your Favorite Number:
    <input type= "text" name = "number" value = "0">
    <br> <br>
    <input type = "submit" value = "Submit"
</div>
</form>
</htm>
"""
    return i


@app.route('/result', methods= ['POST', 'GET'])
def doubled_num():
    if request.method == 'GET':
        double = request.args
        favorite = double.get('number')
        multiply = 2 * (int(favorite))
        return "Double your favorite number is {}".format(multiply)

#@app.route('/result', methods= ['POST', 'GET'])
#def doubled():
#    if request.method == 'GET':
#        double = request.args
#        favorite = double.get('number')
#        multiply = 2 * (int(favorite))
#        return "Double your number is {}".format(multiply)"""
## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable
#than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
    # Month
    # <input type = "text" name = " Month " value = "0" <br><br>
    # Day
    # <input type = "text" name = "Day" value = "0" <br><br>

@app.route('/horoscope', methods = ['POST', 'GET'])
def assign():
    h = """<DOCTYPE html>
<html>
<h1> Daily Horoscope </h1>
<body>
<form action = "/horoscopemessage" method = "GET">
<div>
    Enter your Name:
    <input type = "text" name = "name" value = "Name"
    <br><br>
    <br><br>
    Select Your Sign:
    <br> <br>
    <input type= "radio" name = "options" value = "Aries"> Aries <br>
    <input type= "radio" name = "options" value = "Taurus"> Taurus <br>
    <input type= "radio" name = "options" value = "Gemini"> Gemini <br>
    <input type= "radio" name = "options" value = "Cancer"> Cancer <br>
    <input type= "radio" name = "options" value = "Leo"> Leo<br>
    <input type= "radio" name = "options" value = "Virgo"> Virgo <br>
    <input type= "radio" name = "options" value = "Libra"> Libra <br>
    <input type= "radio" name = "options" value = "Scorpio"> Scorpio <br>
    <input type= "radio" name = "options" value = "Sagittarius"> Sagittarius <br>
    <input type= "radio" name = "options" value = "Capricorn"> Capricorn <br>
    <input type= "radio" name = "options" value = "Aquarius"> Aquarius <br>
    <input type= "radio" name = "options" value = "Pisces"> Pisces <br>



    <br> <br>
    <input type = "submit" value = "Submit"
</div>
</form>
</html>
"""
    return h


@app.route('/horoscopemessage', methods = ['POST', 'GET'])
def fetchsign():
    if request.method == 'GET':
        result = request.args
        horsign = result.get('options')
        name = result.get('name')


        if horsign == "Aries":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Aries'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Taurus":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Taurus'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Gemini":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Gemini'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Cancer":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Cancer'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Leo":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Leo'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Virgo":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Virgo'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Libra":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Libra'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Scorpio":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Scorpio'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Sagittarius":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Sagittarius'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Capricorn":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Capricorn'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Aquarius":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Aquarius'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)

        elif horsign == "Pisces":
            base = 'http://horoscope-api.herokuapp.com/horoscope/today/Pisces'
            response = requests.get(base)
            data = json.loads(response.text)
            message = data['horoscope']
            return "Horoscope: {}".format(message)




if __name__ == '__main__':
    app.run()
