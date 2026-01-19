from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy

import requests

app = Flask(__name__)
app.debug= True

#configure SQlite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contactform.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #avoids a warning 

#creates SQLALchemy instance 

db = SQLAlchemy(app)

#model 
class Contact(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), unique=False, nullable=False)
  last_name = db.Column(db.String(20), unique=False, nullable=False )
  email = db.Column(db.String(50), unique=False, nullable=False )
  message = db.Column(db.String(300), unique=False, nullable=False )
  category = db.Column(db.String(30), unique=False, nullable=False )

  def __repr__(self):
    return f"<Contact : {self.first_name,} {self.last_name}>"

#indexpage route 
@app.route("/")
def index():
  return render_template("index.html")

#contactpage route 
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

    return redirect(url_for("submit"))
  
  return render_template("contact.html")

@app.route("/submit", methods=["GET"])
def submit():
  contacts = db.session.query(Contact).order_by(Contact.id.desc()).all()

  #https://stackoverflow.com/questions/45167508/flask-template-for-loop-iteration-keyvalue


  #used different database 
  # conn = sqlite3.cnnect("contactform.db")
  # cursor = conn.cursor()
  # cursor.excecute("SELECT first_name, category, message FROM contact; ")
  # contacts =cursor.fetchall()
  # conn.close()
  # contacts =""
  return render_template("submit.html", contacts=contacts)


#route for experiments 
@app.route("/experiments")
def experiments():
  return render_template("experiments.html")

#route for cosmetics experiments 
@app.route("/cosmetics")
def cosmetics():
  return render_template("cosmetics.html")

#route for food  experiments 
@app.route("/food")
def food():
  return render_template("food.html")

#route for fun experiments
@app.route("/fun")
def fun():
  return render_template("fun.html")

#bathbomb route 
@app.route("/bathbomb")
def bathbomb():
  return render_template("bathbomb.html")

#route soap 
@app.route("/soap")
def soap():
  return render_template("soap.html")

#route scrub
@app.route("/scrub")
def scrub():
  return render_template("scrub.html")

#route crystals
@app.route("/crystals")
def crystals():
  return render_template("crystals.html")

#route hotice
@app.route("/hotice")
def hotice():
  return render_template("hotice.html")

#route elephanttoothpaste 
@app.route("/elephanttoothpaste")
def elephanttoothpaste():
  return render_template("elephanttoothpaste.html")

#route icecream
@app.route("/icecream")
def icecream():
  return render_template("icecream.html")

#route lavalamp
@app.route("/lavalamp")
def lavalamp():
  return render_template("lavalamp.html")

#route straberrydna
@app.route("/strawberrydna")
def strawberrydna():
  return render_template("strawberrydna.html")

#route poppingboba
@app.route("/poppingboba")
def poppingboba():
  return render_template("poppingboba.html")

#route instantslushie 
@app.route("/instantslushie")
def instantslushie():
  return render_template("instantslushie.html")

#dishwashtabs route
@app.route("/dishwashertabs")
def dishwashertabs():
  return render_template("dishwashertabs.html")

#slime route
@app.route("/slime")
def slime():
  return render_template("slime.html")

#compass route
@app.route("/compass")
def compass():
  return render_template("compass.html")

#mozarella route 
@app.route("/mozarella")
def mozarella():
  return render_template("mozarella.html")

#mozarella route 
@app.route("/mayo")
def mayo():
  return render_template("mayo.html")

#facemask route 
@app.route("/facemask")
def facemask():
  return render_template("facemask.html")


#essentailoil royte 
@app.route("/essentialoil")
def essentialoil():
  return render_template("essentialoil.html")


# @app.route("/login")
# def login():
#   return render_template("login.html") 
# Not used as Just wanted to have a contact form and I thought it would be easy to make another database within



#about us route 
@app.route("/aboutus")
def aboutus():
  return render_template("aboutus.html")

#JSON request for periodictable 
@app.route("/periodictable", methods = ["GET", "POST"])
def periodictable():
  #API endpoint 
  URL= "https://ptable.com/JSON/properties-951c835.json"

  #get request and saving response as object. 
  r = requests.get(URL)

#json extraction
  elements  = r.json()

  elementsearch = None 
  if request.method =="POST":
    elementsearch = request.form.get ("elementsearch")
  return render_template("periodictable.html", elements = elements , elementsearch = elementsearch)


if __name__=="__main__":
  with app.app_context(): #needed for DB operations 
    db.create_all() #creates the database and tables 
  app.run(debug=True)


#https://www.geeksforgeeks.org/python/connect-flask-to-a-database-with-flask-sqlalchemy/
#https://www.geeksforgeeks.org/python/get-post-requests-using-python/ 