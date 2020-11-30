from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.car import Car
import repositories.car_repository as car_repository


cars_blueprint = Blueprint("cars", __name__)

@cars_blueprint.route("/cars")
def cars():
    cars = car_repository.select_all()
    return render_template("cars/index.html", all_cars=cars)


@cars_blueprint.route("/cars/<id>")
def show(id):
    car = car_repository.select(id)
    car_worked_on_by = car_repository.worked_on_by(car)

    return render_template("cars/show.html", car=car, mechanics=car_worked_on_by)


# NEW
# GET '/cars/new'
@cars_blueprint.route("/cars/new", methods = ['GET'])
def new_car():
    # Render html template for new car
    return render_template('cars/new.html')


# CREATE
# POST '/cars'
@cars_blueprint.route("/cars", methods=['POST'])
def create_car():

    registration_number = request.form['registration_number']
    make = request.form['make']
    model = request.form['model']
    mot_renewal_date = request.form['mot_renewal_date']

    car = Car(registration_number, make, model, mot_renewal_date)

    # send request to save mechanic to database
    car_repository.save(car)

    # return to mechanics webpage
    return redirect('/cars')
    