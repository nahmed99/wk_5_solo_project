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


@repairs_blueprint.route("/repairs/<id>/delete", methods=['POST'])
def delete_repair(id):
    repair_repository.delete(id)
    return redirect("/repairs")

