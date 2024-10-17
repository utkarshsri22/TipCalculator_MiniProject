from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    bill = float(request.form['bill'])
    tip = int(request.form['tip'])
    people = int(request.form['people'])

    # Calculate the total amount each person should pay
    total = round(((bill + ((tip / 100) * bill)) / people), 2)

    # Return the result rounded to 2 decimal places
    return render_template('index.html', total=f"{total:.2f}")

if __name__ == '__main__':
    app.run(debug=True)
