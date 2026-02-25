from flask import Flask, render_template, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Divya@2003",   # put your real password
    database="slot_booking"
)

@app.route("/")
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM slots")
    slots = cursor.fetchall()
    return render_template("index.html", slots=slots)


# BOOK SLOT
@app.route("/book/<int:slot_id>")
def book(slot_id):
    cursor = db.cursor()
    cursor.execute("UPDATE slots SET is_booked = TRUE WHERE id = %s", (slot_id,))
    db.commit()
    return redirect("/")


# CANCEL SLOT
@app.route("/cancel/<int:slot_id>")
def cancel(slot_id):
    cursor = db.cursor()
    cursor.execute("UPDATE slots SET is_booked = FALSE WHERE id = %s", (slot_id,))
    db.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)