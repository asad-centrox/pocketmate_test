
from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)
api_key = "api_key"
client = openai.ChatCompletion.create
openai.api_key = api_key

def extract_info(user_prompt):
    subject = user_prompt.split()[0]
    return {"subject": subject}

def update_context(user_prompt, context):
    # Update the context variable with any relevant information extracted from the prompt
    new_info = extract_info(user_prompt)
    context.update(new_info)
    return context

def generate_response(prompt, context, chat_history, temperature, max_tokens):
    # Generate text using the updated messages and adjusted parameters
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].message.content.strip()
    return generated_text

# Initialize the context variable and chat history
context = {}
chat_history = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's prompt from the request body
    user_prompt = request.json['prompt']

    chat_history.append({"role": "user", "content": user_prompt})

    response = generate_response(user_prompt, context, chat_history, 0.8, 200)

    # Add the chatbot's response to the chat history
    chat_history.append({"role": "assistant", "content": response})

    # Log the request and response
    print("prompt:", user_prompt)
    print("chatbot:", response)

    # Return the chatbot's response as a JSON object
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
