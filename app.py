from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route("/experiments")
def experiments():
  return render_template("experiments.html")

@app.route("/cosmetics")
def cosmetics():
  return render_template("cosmetics.html")

@app.route("/food")
def food():
  return render_template("food.html")

@app.route("/fun")
def fun():
  return render_template("fun.html")

if __name__=="__main__":
  app.run(debug=True)

