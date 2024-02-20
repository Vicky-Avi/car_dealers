# car_dealers

Packages to be installed:
=========================
pip install flask sqlalchemy


Packages used:
=============
SQLAlchamy ==> To perform the SQL actions in the flask
datetime   ==> To update current time in the records
enum       ==> Used to specify the status for the records.
Flask      ==> To perform creation of flask applications 
request    ==> Used to get the request params values
jsonify    ==> To convert the response object into json format.

Endpoints:
==========
Also check the endpoints.xlsx, it has the sample requuest details for the reference

POST	     ==> http://localhost:5000/dealers
GET	       ==> http://localhost:5000/dealers
GET	       ==> http://localhost:5000/dealers/{{dealer_id}}
DELETE     ==> http://localhost:5000/dealers/{{dealer_id}}
PUT, PATCH ==> http://localhost:5000/dealers/{{dealer_id}}
POST	     ==> http://localhost:5000/cars
GET	       ==> http://localhost:5000/cars
GET	       ==> http://localhost:5000/cars/{{record_id}}
DELETE	   ==> http://localhost:5000/cars/{{record_id}}
PUT, PATCH ==> http://localhost:5000/cars/{{record_id}}

