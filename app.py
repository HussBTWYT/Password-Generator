import string
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

## characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(length):
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        try:
            length = int(request.form["length"])
            if length > 0:
                password = f'<p style="font-size: 30px;">Your randomly generated password is: {generate_random_password(length)}</p>'
        except ValueError:
            password = '<p style="color: red; font-size: 30px;">Result: Invalid input. Please enter a valid number.</p>'
        
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
