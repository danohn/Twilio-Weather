import os
import requests
from flask import Flask, request
from weather import get_weather
from twilio.twiml.voice_response import Gather, VoiceResponse


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def welcome_route():
    resp = VoiceResponse()
    gather = Gather(action='/getweather', input='dtmf', timeout=5, num_digits=4)
    gather.say('Welcome to the Twilio Weather Service. Please enter a 4 digit post code, followed by hash.')
    resp.append(gather)
    return str(resp)

@app.route("/getweather", methods=['POST'])
def weather_route():
    _zip = request.form['Digits']
    resp = VoiceResponse()
    resp.say(get_weather(_zip))
    return str(resp)

if __name__ == "__main__":
    app.run()

