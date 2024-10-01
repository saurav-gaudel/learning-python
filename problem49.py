#Explore the ‘Flask’ module and create a web server using Flask & Python.

#First (pip install -U Flask) in terminal 


from flask import Flask
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

app.run()