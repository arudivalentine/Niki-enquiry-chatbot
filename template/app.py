import requests
from flask import Flask, render_template, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    response = get_chat_response(msg)
    return jsonify({'response': response})

def get_chat_response(text):
    # Make API call to OpenAI for chat generation
    headers = {
        "Authorization": "Bearer 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",
        "OpenAI-Organization": "org-cmk8cdV1jDX11T4pQnhbv4qi"
    }
    data = {
        "inputs": {
            "text": text
        }
    }
    response = requests.post("https://api.openai.com/v1/models/your-model-id/completions", headers=headers, json=data)
    response_json = response.json()
    completion_text = response_json["choices"][0]["text"].strip()

    return completion_text

if __name__ == '__main__':
    app.run()
