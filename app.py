from flask import Flask, render_template

app = Flask(__name__)

base_url = "https://dev-careers-website.amitsolankideve.repl.co"

@app.route('/')
def home():
    return render_template("home.html", base_url=base_url)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)