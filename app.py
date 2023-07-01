"""
#intents imported from this file itslelf(the responce imported the user must be exactly the same)

from flask import Flask, render_template, request

app = Flask(__name__)

# Define routes and views here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # Process user input and generate a response
    # Replace this logic with your own chatbot implementation
    if user_input.lower() == 'hi':
        response = 'Hello!'
    else:
        response = "I'm sorry, I didn't understand that."

    return response

if __name__ == '__main__':
    app.run()
"""

#importing intents from a json file.

import json
import random
from flask import Flask, render_template, request

app = Flask(__name__)

# Load intents from intents.json file
with open('intents.json') as file:
    intents = json.load(file)['intents']

# Define routes and views here
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    intent = recognize_intent(user_input)

    # Generate a response based on the recognized intent
    if intent is not None:
        response = random.choice(intent['responses'])
    else:
        response = "I'm sorry, I didn't understand that. If this repeats, try to re-phrase your wordings."

    return response

def recognize_intent(user_input):
    # Perform intent recognition based on user input
    for intent in intents:
        for example in intent['examples']:
            if example.lower() in user_input.lower():
                return intent
    return None

if __name__ == '__main__':
    app.run()
