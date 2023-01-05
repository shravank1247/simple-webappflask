import os
from flask import Flask
app = Flask(__name__)

color = os.environ.get('COLOR')

@app.route("/")
def main():
    print(color)
    return render_template('Hello.html', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
