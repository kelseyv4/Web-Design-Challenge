# Dependencies
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ


load_dotenv()

# Create Flask Instance
app = Flask(__name__)

# Add Database
#app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DATABASE_URL", "<postgresql+psycopg2://username:password@host:port/database>")

# Initialize the Database
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/cloudiness")
def about():
    return render_template("cloudiness.html")

@app.route("/comparisons")
def generation():
    return render_template("comparisons.html")

@app.route("/data")
def team():
    return render_template("data.html")

@app.route("/humidity")
def type():
    return render_template("humidity.html")

@app.route("/temp")
def type():
    return render_template("temp.html")

@app.route("/wind")
def type():
    return render_template("wind.html")

if __name__ == "__main__":
    app.run(debug=True)