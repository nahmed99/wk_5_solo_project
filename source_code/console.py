# BEFORE RUNNING THIS PROGRAM, MAKE SURE THAT YOU HAVE CREATED THE REQUIRED DATABASE (using: createdb database_name):
#
# createdb garage_management 
#
# 
# If you have already created your database, and need to delete it, use:
#
#   dropdb database_name
#
#
#
# CREATE THE TABLES (using: psql -d database_name -f filename.sql):
# psql -d garage_management -f db/garage_management.sql
#
# Then run this file as a normal python program...
#
# And then you can run flask and check localhost:5000/
#
# flask run
#
#
# Any issues, then you could type in the following commands (in terminal):
# psql  (to launch psql terminal)
# \c database_name  (to connect to the db)
# select * from table;  (or any other sql commands...)
#  
#  or you can use: psql -d garage_management
# 
# To access the database:
#
# psql -d database_name
#
#
# The following command might be useful at some point:
#
#   rm -f /usr/local/var/postgres/postmaster.pid
#

import pdb

from models.car import Car
from models.mechanic import Mechanic
from models.repair import Repair


import repositories.repair_repository as repair_repository
import repositories.mechanic_repository as mechanic_repository
import repositories.car_repository as car_repository


# delete the repairs first - for referential integrity purposes (they reference the other tables)
repair_repository.delete_all()


# create mechanic, car and repair objects and then use them to create rows/records on db

# mechanics
mechanic_mot = Mechanic("Thomas", "Brown", True)
mechanic_repository.save(mechanic_mot)

mechanic_no_mot = Mechanic("Roger", "Rabbit", False)
mechanic_repository.save(mechanic_no_mot)

mechanic_3 = Mechanic("Spanner", "Joe", False)
mechanic_repository.save(mechanic_3)


# cars

car_1 = Car("ZZ99 NEW", "Ford", "Escort", "2021-05-15")
car_repository.save(car_1)

car_2 = Car("AA11 OLD", "Lada", "L11", "2021-03-23")
car_repository.save(car_2)

car_3 = Car("XY55 QWT", "Toyota", "Avensis", "2021-11-01")
car_repository.save(car_3)

car_4 = Car("F123 XYZ", "Vauxhall", "Zafira", "2020-12-29")
car_repository.save(car_4)

car_5 = Car("A1 1A", "Fiat", "Puddle Jumper", "2021-06-07")
car_repository.save(car_5)


# repairs

repair_1 = Repair("2020-10-07", "Full service", mechanic_no_mot, car_4)
repair_repository.save(repair_1)

repair_2 = Repair("2020-10-23", "Replace water pump", mechanic_mot, car_1)
repair_repository.save(repair_2)

repair_3 = Repair("2020-11-01", "Full service", mechanic_no_mot, car_5)
repair_repository.save(repair_3)

repair_4 = Repair("2020-11-05", "Service", mechanic_3, car_3)
repair_repository.save(repair_4)

repair_4a = Repair("2020-11-05", "MOT", mechanic_mot, car_3)
repair_repository.save(repair_4a)

repair_5 = Repair("2020-11-14", "New gear box", mechanic_3, car_2)
repair_repository.save(repair_5)

repair_6 = Repair("2020-11-16", "Puncture repair", mechanic_mot, car_4)
repair_repository.save(repair_6)

repair_7 = Repair("2020-11-21", "Replaced spark plugs, air, oil and fuel filters, and oil", mechanic_no_mot, car_1)
repair_repository.save(repair_7)

repair_8 = Repair("2020-11-22", "New clutch", mechanic_no_mot, car_2)
repair_repository.save(repair_8)


# for testing/tracing:
pdb.set_trace()
