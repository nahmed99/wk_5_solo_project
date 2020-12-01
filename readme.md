Running Instructions
====================

Prior to running this app, the following software is required:

- Python
- A suitable web browser
- Postgre DB
- Flask

The instructions are:

- Create the required database:

createdb garage_management


- Create the required tables (by running the following command from the top directory):

psql -d garage_management -f db/garage_management.sql


- You can run the following program to 'seed' the database:

python3 console.py


- Run flask

flask run


- View the app on a web broswer at the following address:

localhost:5000/





The Brief
=========

Garage Management App
*********************

A local garage has approached you to build a web application to help them manage their mechanics and workload. A mechanic may repair many cars at a time. A car can be repaired by many mechanics at the same (or over a longer period of) time.

MVP
The garage wants to be able to register / track repairs. Important information for the management to know is -

= Mechanic =
- First Name
- Last Name
- Whether or not MOT qualified

= Car = 
- Registration Number
- Make
- Model
- MOT Renewal Date (not essential, but useful for potential future follow up work)

= Repairs =
- Date of Repair
- Vehicle Repaired
- Mechanic 
- Details of Repair


The management must be able to create records of repairs, linking mechanics to the cars.

CRUD actions for repairs - remember the user - what would they want to see on each View? What Views should there be?


Possible Extensions
*********************

- Be able to view multiple repairs carried out by a mechanic to a particular car
- Be able to view multiple (including historic) repairs done to a car by a particular mechanic
- Be able to toggle a mechanic's MOT qualification status
- Be able to add and delete mechanics
- Be able to add new cars 
- Create Owner class and link owner details to the cars (one to many relationship)
- Display data in sorted order (date(s), mot qualification status order etc)


 Technologies Used 
*******************
- Python
- PostGre SQL DB
- Flask
- HTML
- CSS
