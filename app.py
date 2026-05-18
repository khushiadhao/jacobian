from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

number_to_guess = random.randint(1, 100)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global number_to_guess
    data = request.get_json()
    user_guess = int(data['guess'])

    if user_guess < number_to_guess:
        return jsonify({"result": "Too Low!"})
    elif user_guess > number_to_guess:
        return jsonify({"result": "Too High!"})
    else:
        number_to_guess = random.randint(1, 100)
        return jsonify({"result": "Correct! 🎉 New number generated."})

if __name__ == '__main__':
    app.run(debug=True)
