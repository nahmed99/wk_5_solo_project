from flask import Flask, render_template, request
from flask import Blueprint
from models.mechanic import Mechanic
import repositories.mechanic_repository as mechanic_repository

mechanics_blueprint = Blueprint("mechanics", __name__)

@mechanics_blueprint.route("/mechanics")
def mechanic():
    mechanics = mechanic_repository.select_all()

    return render_template("mechanics/index.html", all_mechanics = mechanics)


@mechanics_blueprint.route("/mechanics/<id>")
def show(id):
    mechanic = mechanic_repository.select(id)
    mechanic_cars_repaired = mechanic_repository.cars_repaired(mechanic)

    return render_template("mechanics/show.html", mechanic=mechanic, cars_repaired=mechanic_cars_repaired)