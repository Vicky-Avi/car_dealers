from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
from enum import Enum


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///car_world.db'  # SQLite database file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Dealers(db.Model):
    """
        Dealers table contains the agent or company names where the cars are going  to sell.
    """
    __tablename__ = 'dealers_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    mobile = db.Column(db.BigInteger, nullable=False)
    alternate_number = db.Column(db.BigInteger, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    gst_number = db.Column(db.String(100), nullable=True)
    tin_number = db.Column(db.String(100), nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.now())
    
class CarStatus(Enum):
    open = 'open'
    booked = 'booked'
    delivered = 'delivered'
    cancelled = 'cancelled'

class Cars(db.Model):
    """
        Cars table have the car details with respected to dealers
    """
    __tablename__ = 'cars_table'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    seater = db.Column(db.Integer, nullable=False)
    number = db.Column(db.String(100), nullable=False)
    dealer_id = db.Column(db.ForeignKey("dealers_table.id"), nullable=False)
    status = db.Column(db.Enum(CarStatus), nullable=False, default=CarStatus.open)
    booked_date = db.Column(db.DateTime, nullable=True)
    delivered = db.Column(db.Boolean, default=False)
    delivered_date = db.Column(db.DateTime, nullable=True)
    cancelled_date = db.Column(db.DateTime, nullable=True)
    created_on = db.Column(db.DateTime, default=datetime.now())
    updated_on = db.Column(db.DateTime, default=datetime.now())
    available = db.Column(db.Boolean, default=True)


sample_tasks = [
    Dealers(name='ABC Motors', email="abc@gmail.com", mobile="+91-984738473", alternate_number="", address=""),
    Dealers(name='XYZ Dealers', email="abc@gmail.com", mobile="+91-984738473", alternate_number="", address=""),
    Dealers(name='MVP Cars', email="abc@gmail.com", mobile="+91-984738473", alternate_number="", address=""),
]




with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.bulk_save_objects(sample_tasks)
    db.session.commit()