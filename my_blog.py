from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/birthday')
def birthday():
    return app.send_static_file("birthday.html")

@app.route('/greeting/<user>')
def greeting(user):
    return render_template('greeting.html', user=user)

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    total = num1 + num2
    return render_template('calculation_results.html', total= str(total))

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    total = num1 * num2
    return render_template('calculation_results.html', total= str(total))

@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    total = num1 - num2
    return render_template('calculation_results.html', total= str(total))

@app.route('/favoritefoods')
def favoritefoods():
    my_fav_foods = [
        "pasta",
        "sushi",
        "ice cream"
    ]
    return jsonify(my_fav_foods)

if __name__ == "__main__":
    app.run()
