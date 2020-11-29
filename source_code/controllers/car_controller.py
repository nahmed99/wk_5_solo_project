from flask import Flask, render_template, request
from flask import Blueprint
from models.car import Car
import repositories.car_repository as car_repository


cars_blueprint = Blueprint("cars", __name__)

@cars_blueprint.route("/cars")
def cars():
    cars = car_repository.select_all()
    return render_template("cars/index.html", all_cars=cars)