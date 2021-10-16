from flask import Flask, render_template, request, redirect, url_for

from random import randrange

import geoLocate

# https://developer.here.com/develop/rest-apis
# https://geopy.readthedocs.io/en/stable/#Nominatim

'''
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
'''

app = Flask(__name__)

'''
class AddressForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Submit')
'''

def getCity(address):
    # "city","city_ascii","lat","lng","country","iso2","iso3","admin_name","capital","population","id"

    processed_text = ""
    randomInt = randrange(1, 26571)
    counter = 0

    with open('static/database/worldcities.csv', 'r', encoding="utf8") as reader:
        for line in reader:

            if counter == randomInt:
                splitLine = line.split(",")
                # processed_text = splitLine[1]
                processed_text = splitLine
                break
            counter += 1


    coords = geoLocate.convertAddress(address)
    distance = geoLocate.getDistance(processed_text, coords)
    destAddress = geoLocate.convertAddress(processed_text[1])

    return render_template('destination.html',
                city=processed_text[1], distance=distance, coords=coords, destAddress=destAddress, startAddress=address)

@app.route("/")
def landing():
    return render_template('/index.html')


@app.route('/', methods=['POST'])
def index():
    text = request.form['subscribe_email']
    address = text.upper()
    return getCity(address)





# initially pass in "name", then set name to name.