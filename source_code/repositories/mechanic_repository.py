from db.run_sql import run_sql
from models.mechanic import Mechanic
from models.car import Car


def save(mechanic):
    # We want the database MS to return the (newly created) id
    sql = """INSERT INTO mechanics (first_name, last_name, mot_qualified) 
             VALUES (%s, %s, %s) RETURNING id"""

    values = [mechanic.first_name, mechanic.last_name, mechanic.mot_qualified]

    results = run_sql(sql, values)

    # results are returned as a list of dictionary in our case - capture the id
    mechanic.id = results[0]['id']

    return mechanic


def select(id):
    mechanic = None
    sql = "SELECT * FROM mechanics WHERE id = %s"
    values = [id] # a list is supplied to run_sql

    result = run_sql(sql, values)[0] # ensure only one row is returned.

    if result is not None:
        mechanic = Mechanic(result['first_name'], result['last_name'], result['mot_qualified'], result['id'])

    return mechanic


def select_all():
    mechanics = []

    sql = "SELECT * FROM mechanics"
    results = run_sql(sql)

    for row in results:
        mechanic = Mechanic(row['first_name'], row['last_name'], row['mot_qualified'], row['id'])
        mechanics.append(mechanic)

    return mechanics


def delete(id):
    sql = "DELETE FROM mechanics WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM mechanics"
    run_sql(sql)


# get all cars that the mechanic has repaired
def cars_repaired(mechanic):
    results = []

    sql = """SELECT DISTINCT cars.*
           FROM cars
           INNER JOIN repairs ON repairs.car_id = cars.id
           INNER JOIN mechanics ON repairs.mechanic_id = mechanics.id
           WHERE mechanics.id = %s"""

    values = [mechanic.id]

    sql_results = run_sql(sql, values)

    for row in sql_results:
        car = Car(row['registration_number'], row['make'], row['model'], row['mot_renewal_date'], row['id'])
        results.append(car)

    return results


def mot_toggle(id):
    mechanic = select(id)
    if mechanic != None:
        toggled_mot_qualified = not mechanic.mot_qualified

    # For some VERY strange reason, PostgreSQL won't let you update a single column in a multi-column table, without using a sub-select or a row()..? A bit late in the day, so 'amended' two columns just to get past this - need to find out how to use the Row() expression...

    sql = "UPDATE mechanics SET (mot_qualified, first_name) = (%s, %s) WHERE id = %s RETURNING id"
    values = [toggled_mot_qualified, mechanic.first_name, id]
    run_sql(sql, values)

