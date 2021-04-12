# Twilio Weather

Twilio Weather is a Flask app which returns a weather annoucement in the form of TwiML, used by Twilio for incoming calls. Weather data is provided by [OpenWeather](https://openweathermap.org/api).

## Getting Started
To run Twilio Weather, you will need an OpenWeather API key from [here](https://openweathermap.org/api). The Free subscription is fine to start off with. The key needs to exist as an Environment Variable named `OPEN_WEATHER_MAP_API_KEY`.

Once the API key is set as an Environment Variable, start the local Flask server by running `app.py`. Once running, you will need to expose the service to the internet. This can be achieved with tools such as [ngrok](https://ngrok.com/).

## More info
When you call your Twilio number, Twilio will send a WebHook request to the Flask server and you will be prompted to enter a 4 digit post code (currently the script supports Australian post codes). Once Twilio completes gathering the digits, another request will be sent to the `getweather` Flask route.
