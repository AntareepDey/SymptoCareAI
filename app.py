from flask import Flask, render_template,request, redirect, url_for, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def hello():
    return render_template('home.html')

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

@app.route('/login')
def login():
    return '<h1>Login Page</h1>'

@app.route('/chatbot',methods=['GET','POST'])
def chatbot():
    return render_template('chatbot.html')
    


if __name__ == "__main__":
  app.run(debug=True)