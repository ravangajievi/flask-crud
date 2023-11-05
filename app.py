from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class Person:
    def __init__(self, name):
        self.name = name

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_name = request.form['username']
        person = Person(user_name)
        
        return render_template("greeting.html", name=person.name)
    
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
