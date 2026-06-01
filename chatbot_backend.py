from flask import Flask, request, jsonify
from flask_cors import CORS
import http.client
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend requests

API_KEY = "f8dfa13fd7918be1365c33f136e7a5c1bb743d352dc70c445bce0db9a3cee365"

def chat_with_bot(prompt):
    conn = http.client.HTTPSConnection("api.together.xyz")
    payload = json.dumps({
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are Bytie, a helpful study assistant designed to help students with their academic questions, provide motivation, and offer study tips. Be friendly, encouraging, and concise in your responses."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    })

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    try:
        conn.request("POST", "/v1/chat/completions", body=payload, headers=headers)
        res = conn.getresponse()
        data = res.read()

        if res.status == 200:
            result = json.loads(data)
            return {"success": True, "message": result['choices'][0]['message']['content']}
        return {"success": False, "message": f"Error: {res.status} - {data.decode()}"}
    except Exception as e:
        return {"success": False, "message": f"Error: {str(e)}"}
    finally:
        conn.close()

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({"success": False, "message": "No message provided"}), 400
    
    return jsonify(chat_with_bot(user_message))

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    print("🤖 Bytie chatbot server starting on http://localhost:5000")
    app.run(debug=True, port=5000)
