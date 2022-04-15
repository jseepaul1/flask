from flask import Flask
app = Flask(__name__)

# localhost:5000/ - have it say "Hello World!"


@app.route('/')
def hello_world():
    return 'Hello World!'

# localhost:5000/dojo - have it say "Dojo!"


@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"


@app.route('/say/<name>')
def change_name(name):
    return f"Hi {name}!"

# Create one url pattern and function that can handle the following examples
# (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times


@app.route('/repeat/<int:num>/<string:word>')  #NINJA BONUS: Ensure the names provided in the 3rd task are strings
def repeat(num, word):
    return f"{num * word}"


if __name__ == "__main__":
    app.run(debug=True)
