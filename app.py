from flask import Flask, render_template,request, redirect, url_for, jsonify
import requests
from medisearch_client import MediSearchClient
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

api_key = ''
client = MediSearchClient(api_key=api_key)

@app.route('/home')
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
    # data = request.json
    # user_message = data.get("message")[0]
    conversation_id = str(uuid.uuid4())
    if request.headers.get('Content-Type') == 'application/json':
        data = request.json
        user_message = data.get("message")
        # Send the user message to MediSearch
        responses = client.send_user_message(
            conversation=[user_message],
            conversation_id=conversation_id,
            should_stream_response=False,
            language="English"
        )
        # Process responses from MediSearch
        response_text = ""
        for response in responses:
            if response["event"] == "llm_response":
                llm_answer = response["text"]
                response_text += llm_answer + "\n"
        return jsonify({"response": response_text})
    else:
        return jsonify({"error": "Unsupported Media Type"}), 415  # Return a 415 status code for Unsupported Media Type



if __name__ == "__main__":
  app.run(debug=True)