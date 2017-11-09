#Tiffany Moi
#SoftDev1 pd7
#HW13--A RESTful Journey Skyward
#2017-11-09

from flask import Flask, render_template
import urllib2, json

uResp = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=sCOQtPYKmZp1EgtE4GsyDoIlaQ0fUo9vijo2Fyxp")

#print uResp.geturl()
#print uResp.info()
info = json.loads(uResp.read())

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('space.html', img = info['url'], descrip = info['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()
