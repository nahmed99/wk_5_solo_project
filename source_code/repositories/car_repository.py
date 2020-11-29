from db.run_sql import run_sql
from models.car import Car
from models.mechanic import Mechanic


def save(car):
    sql = "INSERT INTO cars(registration_number, make, model, mot_renewal_date) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [car.registration_number, car.make, car.model, car.mot_renewal_date]

    results = run_sql(sql, values)

    car.id = results[0]['id']

    return car


def select_all():
    cars = []

    sql = "SELECT * FROM cars"
    results = run_sql(sql)

    for row in results:
        car = Car(row['registration_number'], row['make'], row['model'], row['mot_renewal_date'], row['id'])
        cars.append(car)

    return cars