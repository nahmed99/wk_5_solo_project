from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.repair import Repair

import repositories.repair_repository as repair_repository
import repositories.mechanic_repository as mechanic_repository
import repositories.car_repository as car_repository

repairs_blueprint = Blueprint("repairs", __name__)

@repairs_blueprint.route("/repairs")
def repairs():
    repairs = repair_repository.select_all()
    return render_template("/repairs/index.html", all_repairs = repairs)


@repairs_blueprint.route("/repairs/<mechanic_id>/<car_id>")
def show(mechanic_id, car_id):
    repairs = repair_repository.get_rapair_details(mechanic_id, car_id)
    return render_template("/repairs/show.html", car_repairs = repairs)


@repairs_blueprint.route("/repairs/search", methods=['GET'])
def search():
    # Need to use the args function to extract data from query string (for GET)!!!
    search_string = request.args["search_string"]
    repairs = repair_repository.search(search_string)

    # If nothing returned from the search, then display the full repairs list
    if len(repairs) > 0:
        return render_template("/repairs/index.html", all_repairs = repairs)
    else:
        return redirect('/repairs')



# NEW
# GET '/repairs/new'
@repairs_blueprint.route("/repairs/new", methods = ['GET'])
def new_repair():
    # Get list of mechanics - for user to select from (when creating new repair)
    mechanics = mechanic_repository.select_all()

    # Get list of cars for user to select from (when creating new repair)
    cars = car_repository.select_all()

    # Render html template, sending data to it. 
    return render_template('repairs/new.html', all_mechanics=mechanics, all_cars = cars)


# CREATE
# POST '/repairs'
@repairs_blueprint.route("/repairs", methods=['POST'])
def create_repair():
    repair_date = request.form['repair_date']
    details = request.form['details']

    # 'extract' mechanic_id and request retrieval of its class
    mechanic_id = request.form['mechanic_id']
    mechanic = mechanic_repository.select(mechanic_id)

    # 'extract' car_id and request retrieval of its class
    car_id = request.form['car_id']
    car = car_repository.select(car_id)

    # create repair object
    repair = Repair(repair_date, details, mechanic, car)

    # send request to save repair to database
    repair_repository.save(repair)

    # return to reapirs webpage
    return redirect('/repairs')


# EDIT
@repairs_blueprint.route("/repairs/<id>/edit")
def edit_repair(id):
    
    # Gather data
    repair = repair_repository.select(id)
    
    # need to send details of all mechanics and cars so that user can
    # choose them from drop-down lists.
    mechanics = mechanic_repository.select_all()
    cars = car_repository.select_all()

    # Send date to edit page
    return render_template('repairs/edit.html', repair=repair, all_mechanics=mechanics, all_cars=cars)


# UPDATE
@repairs_blueprint.route("/repairs/<id>", methods=["POST"])
def update_repair(id):

    repair_date = request.form['repair_date']
    details =  request.form['details']

    machanic_id = request.form["mechanic_id"]
    mechanic = mechanic_repository.select(machanic_id)

    car_id = request.form["car_id"]
    car = car_repository.select(car_id)

    # create repair object
    repair = Repair(repair_date, details, mechanic, car, id)

    # update repair on database
    repair_repository.update(repair)

    # send control back to repairs page
    return redirect("/repairs")


@repairs_blueprint.route("/repairs/<id>/delete", methods=['POST'])
def delete_repair(id):
    repair_repository.delete(id)
    return redirect("/repairs")

