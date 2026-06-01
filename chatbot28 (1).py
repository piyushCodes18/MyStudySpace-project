import http.client
import json

API_KEY = "f8dfa13fd7918be1365c33f136e7a5c1bb743d352dc70c445bce0db9a3cee365"

def chat_with_bot(prompt):
    conn = http.client.HTTPSConnection("api.together.xyz")
    payload = json.dumps({
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    })

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    conn.request("POST", "/v1/chat/completions", body=payload, headers=headers)
    res = conn.getresponse()
    data = res.read()

    if res.status == 200:
        result = json.loads(data)
        return result['choices'][0]['message']['content']
    return f"Error: {res.status} - {data.decode()}"

print("Bytie is here to help you! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    print("Bot:", chat_with_bot(user_input))
