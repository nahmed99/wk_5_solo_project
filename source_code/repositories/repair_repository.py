from db.run_sql import run_sql
from models.repair import Repair

import repositories.mechanic_repository as mechanic_repository
import repositories.car_repository as car_repository


def save(repair):
    sql = """INSERT INTO repairs ( mechanic_id, car_id, repair_date, details) 
             VALUES (%s, %s, %s, %s) RETURNING id"""
    
    values = [repair.mechanic.id, repair.car.id, repair.repair_date, repair.details]

    results = run_sql(sql, values)
    repair.id = results[0]['id']
    return repair


def select(id):
    repair = None
    sql = "SELECT * FROM repairs WHERE id = %s ORDER BY repair_date DESC"
    values = [id] # a list is supplied to run_sql

    result = run_sql(sql, values)[0] # ensure only one row is returned.

    if result is not None:
         # using mechanic_id from repairs, retrieve mechanic object
        mechanic = mechanic_repository.select(result['mechanic_id'])

        # using car_id from repairs, retrieve car object
        car = car_repository.select(result['car_id'])

        # create Repair object, assign to variable 'repair'
        repair = Repair(result['repair_date'], result['details'], mechanic, car, result['id'])

    return repair


def select_all():

    # create empty list
    repairs = []

    sql = "SELECT * FROM repairs ORDER BY repair_date DESC"
    results = run_sql(sql)

    for row in results:
        # using mechanic_id from repairs, retrieve mechanic object
        mechanic = mechanic_repository.select(row['mechanic_id'])

        # using car_id from repairs, retrieve car object
        car = car_repository.select(row['car_id'])

        # create Repair object, assign to variable 'repair'
        repair = Repair(row['repair_date'], row['details'], mechanic, car, row['id'])

        repairs.append(repair)

    return repairs


def search(search_string):
    repairs = []

    if len(search_string) > 0:
        sql = "SELECT * FROM repairs WHERE details LIKE %s ORDER BY repair_date DESC"
        new_search_string = '%' + search_string + '%'
        values = [new_search_string] 

        results = run_sql(sql, values)

        for row in results:
            mechanic = mechanic_repository.select(row['mechanic_id'])
            car = car_repository.select(row['car_id'])

            # create Repair object, assign to variable 'repair'
            repair = Repair(row['repair_date'], row['details'], mechanic, car, row['id'])

            repairs.append(repair)

    return repairs


def update(repair):
    sql = "UPDATE repairs SET (repair_date, details, mechanic_id, car_id) = (%s, %s, %s, %s) WHERE id = %s RETURNING id"

    values = [repair.repair_date, repair.details, repair.mechanic.id, repair.car.id, repair.id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM repairs"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM repairs WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def get_rapair_details(mechanic_id, car_id):
    repairs = []

    # using mechanic_id from repairs, retrieve mechanic object
    mechanic = mechanic_repository.select(mechanic_id)

    # using car_id from repairs, retrieve car object
    car = car_repository.select(car_id)
    

    sql = "SELECT * FROM repairs WHERE mechanic_id = %s AND car_id = %s"
    values = [mechanic_id, car_id] # a list is supplied to run_sql

    results = run_sql(sql, values)
    
    for row in results:
        # create Repair object, assign to variable 'repair'
        repair = Repair(row['repair_date'], row['details'], mechanic, car, row['id'])

        repairs.append(repair)

    return repairs
