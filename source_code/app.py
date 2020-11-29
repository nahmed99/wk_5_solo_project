from flask import Flask, render_template

from controllers.mechanic_controller import mechanics_blueprint
from controllers.car_controller import cars_blueprint
from controllers.repair_controller import repairs_blueprint


app = Flask(__name__)

app.register_blueprint(mechanics_blueprint)
app.register_blueprint(cars_blueprint)
app.register_blueprint(repairs_blueprint)


@app.route('/')
def homw():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)