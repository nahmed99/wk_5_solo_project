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

