from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.mechanic import Mechanic
import repositories.mechanic_repository as mechanic_repository

mechanics_blueprint = Blueprint("mechanics", __name__)

@mechanics_blueprint.route("/mechanics")
def mechanic():
    mechanics = mechanic_repository.select_all()

    return render_template("mechanics/index.html", all_mechanics=mechanics)


@mechanics_blueprint.route("/mechanics/<id>")
def show(id):
    mechanic = mechanic_repository.select(id)
    mechanic_cars_repaired = mechanic_repository.cars_repaired(mechanic)

    return render_template("mechanics/show.html", mechanic=mechanic, cars_repaired=mechanic_cars_repaired)



# NEW
# GET '/mechanics/new'
@mechanics_blueprint.route("/mechanics/new", methods = ['GET'])
def new_mechanic():
    # Render html template for new mechanic 
    return render_template('mechanics/new.html')


# CREATE
# POST '/mechanics'
@mechanics_blueprint.route("/mechanics", methods=['POST'])
def create_mechanic():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    mot_qualified = request.form['mot_qualified']
    
    mechanic = Mechanic(first_name, last_name, mot_qualified)

    # send request to save mechanic to database
    mechanic_repository.save(mechanic)

    # return to mechanics webpage
    return redirect('/mechanics')


@mechanics_blueprint.route("/mechanics/<id>/delete", methods=['POST'])
def delete_mechanic(id):
    mechanic_repository.delete(id)
    return redirect("/mechanics")


@mechanics_blueprint.route("/mechanics/<id>/mot_toggle", methods=['POST'])
def mot_toggle(id):
    mechanic_repository.mot_toggle(id)
    return redirect("/mechanics")
