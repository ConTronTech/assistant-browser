# Import necessary modules
from flask import Flask, render_template, request, jsonify
import requests
import json

# Initialize Flask app
app = Flask(__name__)

# Function to send a request to the model
def send_request(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "llama2-uncensored",
        "prompt": prompt
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        response_lines = response.text.strip().split('\n')
        json_objects = [json.loads(line) for line in response_lines if line]
        return json_objects
    else:
        print(f"Failed to get a successful response. Status code: {response.status_code}")
        return None

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling user input
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']
    response_objects = send_request(user_input)
    if response_objects:
        response_text = ''.join(obj['response'] for obj in response_objects)
        return jsonify({'response': response_text})
    else:
        return jsonify({'error': 'Failed to generate response'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
