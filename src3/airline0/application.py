import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import json


app = Flask(__name__)

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    flights = db.execute("select id, origin, destination, duration from flights order by id").fetchall()
    print(flights)
    return render_template('index.html', flights=flights)

@app.route('/book', methods=['POST'])
def book():
    # Get value and update it to db.
    # get value:
    name = request.form.get('name')
    flight_id = int(request.form.get('flight_id'))
    db.execute("insert into passengers (name, flight_id) VALUES (:name, :flight_id)", {'name': name, 'flight_id': flight_id})
    db.commit()
    return render_template('success.html')

@app.route("/text")
def test():
    return render_template('text.html')



    # <h1>Book a Flight</h1>

    # <form action="{{ url_for('book') }}" method="post">

    #     <div class="form-group">
    #         <select class="form-control" name="flight_id">
    #             {% for flight in flights %}
    #                 <option value="{{ flight.id }}">{{ flight.origin }} to {{ flight.destination }}</option>
    #             {% endfor %}
    #         </select>
    #     </div>

    #     <div class="form-group">
    #         <input class="form-control" name="name" placeholder="Passenger Name">
    #     </div>

    #     <div class="form-group">
    #         <button class="btn btn-primary">Book Flight</button>
    #     </div>

    # </form>






# @app.route("/")
# def index():
#     flights = db.execute("SELECT * FROM flights").fetchall()
#     return render_template("index.html", flights=flights)

# @app.route("/book", methods=["POST"])
# def book():
#     """Book a flight."""

#     # Get form information.
#     name = request.form.get("name")
#     try:
#         flight_id = int(request.form.get("flight_id"))
#     except ValueError:
#         return render_template("error.html", message="Invalid flight number.")

#     # Make sure the flight exists.
#     if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0:
#         return render_template("error.html", message="No such flight with that id.")
#     db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
#             {"name": name, "flight_id": flight_id})
#     db.commit()
#     return render_template("success.html")

