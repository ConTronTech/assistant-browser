import requests
import json

def get_user_input():
    user_input = input("Enter your question (or type 'exit' to quit): ")
    return user_input

def send_request(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {"Content-Type": "application/json"}
    data = {
        "model": "Jeffery",
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

def main():
    while True:
        user_input = get_user_input()
        if user_input.lower() == 'exit':
            break
        response_objects = send_request(user_input)
        if response_objects:
            response_text = ''.join(obj['response'] for obj in response_objects)
            print(response_text)

if __name__ == "__main__":
    main()
