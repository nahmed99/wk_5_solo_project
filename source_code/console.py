# BEFORE RUNNING THIS PROGRAM, MAKE SURE THAT YOU HAVE CREATED THE REQUIRED DATABASE (using: createdb database_name):
#
# createdb music_library 
#
# 
# If you have already created your database, and need to delete it, use:
#
#   dropdb database_name
#
#
#
# CREATE THE TABLES (using: psql -d database_name -f filename.sql):
# psql -d music_library -f db/music_library.sql
#
# Then run this file as a normal python program...
#
#
# Any issues, then you could type in the following commands (in terminal):
# psql  (to launch psql terminal)
# \c database_name  (to connect to the db)
# select * from table;  (or any other sql commands...)
#  
#  or you can use: psql -d quest_advisor
# 
# To access the database:
#
# psql -d database_name
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


# create mechanic, car and repair rows/records




# for testing/tracing:
pdb.set_trace()
