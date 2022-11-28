from flask import Flask  # lets you get stuff off the web

#Instantiate a flask object 
app = Flask(__name__)

#Define a route
@app.route("/")
def hello():
    return "Hello, World!"

app.run(debug=True)