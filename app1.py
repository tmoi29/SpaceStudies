#Tiffany Moi
#SoftDev1 pd7
#HW14 -- Getting More REST
#2017-11-13

from flask import Flask, render_template, request
import urllib2, json


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/expand')
def expand():
    url = "https://www.googleapis.com/urlshortener/v1/url?key=AIzaSyCrv9b7dDoLSLA_vcRomCgaBrF4UtVVOZo&shortUrl="
    shortUrl = request.args["shortUrl"]
    url = url + shortUrl
    uResp = urllib2.urlopen(url)
    info = json.loads(uResp.read())
    short = info["longUrl"]
    return render_template('results.html', newUrl=short)


if __name__ == "__main__":
    app.debug = True
    app.run()
