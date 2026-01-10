from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#configure SQlite database
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///contactform.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #avoids a warning 

#creates SQLALchemy instance 

db = SQLAlchemy(app)

class Contact(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), unique=False, nullable=False)
  last_name = db.Column(db.String(20), unique=False, nullable=False )
  email = db.Column(db.String(20), unique=False, nullable=False )
  message = db.Column(db.String(300), unique=False, nullable=False )
  category = db.Column(db.String(20), unique=False, nullable=False )

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/contact", methods=["GET", "POST"])
def contact_page():
  if request.method =="POST":
    first_name = request.form ["first_name"]
    last_name = request.form["last_name"]
    email= request.form["email"]
    message = request.form["message"]
    category = request.form ["category"]

    new_contact = Contact (
      first_name = first_name,
      last_name = last_name,
      email=email,
      message = message,
      category = category)
    
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for("index"))
  
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
  with app.app_context(): #needed for DB operations 
    db.create_all() #creates the database and tables 
  app.run(debug=True)


#https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/