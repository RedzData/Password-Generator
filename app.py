from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def random_password_generator(length):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to include all required character types.")

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    remaining_length = length - 4
    if remaining_length > 0:
        all_characters = string.ascii_letters + string.digits + string.punctuation
        password += [random.choice(all_characters) for _ in range(remaining_length)]

    random.shuffle(password)
    return ''.join(password)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = data.get('length')
    try:
        password = random_password_generator(length)
        return jsonify({'password': password})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
