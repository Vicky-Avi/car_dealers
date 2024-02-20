from flask import jsonify, request
from datetime import datetime
from sql import *

@app.route('/dealers', methods=['GET'])
def get_dealers():
    """
        Get all dealers without any condition
    """
    all_dealers = Dealers.query.all()
    dealers_data = [{column.name: getattr(dealer, column.name) for column in Dealers.__table__.columns} for dealer in all_dealers]
    return jsonify({'data': dealers_data}), 200

@app.route('/dealers', methods=['POST'])
def create_dealers():
    """
        To create dealers and returning with their details.
    """
    data = request.get_json()
    dealer_obj = Dealers(**data)
    db.session.add(dealer_obj)
    db.session.commit()
    return jsonify({'data': {column.name: getattr(dealer_obj, column.name) for column in Dealers.__table__.columns}}), 201

@app.route('/dealers/<int:dealer_id>', methods=['GET'])
def get_dealer(dealer_id):
    """
        To get particular dealers with their record id.
        dealer_id (int) ==> record id
    """
    dealer_obj = Dealers.query.get(dealer_id)
    if dealer_obj:
        return jsonify({'data': {column.name: getattr(dealer_obj, column.name) for column in Dealers.__table__.columns}}), 200
    else:
        return jsonify({'message': 'Dealer not found'}), 404


@app.route('/dealers/<int:dealer_id>', methods=['DELETE'])
def delete_dealers(dealer_id):
    """
        To remove the particular dealer
        dealer_id (int) ==> record id
    """
    dealer_obj = Dealers.query.get(dealer_id)
    if dealer_obj:
        name = dealer_obj.name
        db.session.delete(dealer_obj)
        db.session.commit()
        return jsonify({'message': f'Dealer {name} deleted successfully'})
    else:
        return jsonify({'error': f'Dealer not found'}), 404

@app.route('/dealers/<int:dealer_id>', methods=['PUT', 'PATCH'])
def update_dealers(dealer_id):
    """
        To update the dealers
        dealer_id (int) ==> record id
    """
    dealer_obj = Dealers.query.get(dealer_id)
    if not dealer_obj:
        return jsonify({'error': f'Dealer not found'}), 404

    data = request.get_json()
    field_names = [column.name for column in Dealers.__table__.columns]    
    for key, value in data.items():
        if hasattr(Dealers, key):
            setattr(dealer_obj, key, value)
    db.session.commit()

    return jsonify({'message': f'Dealer updated successfully'}), 200

@app.route('/cars', methods=['POST'])
def create_cars():
    """
        To perform creation of cars and returning with their details.
    """
    data = request.get_json()
    car_obj = Cars(**data)
    db.session.add(car_obj)
    db.session.commit()
    data = {column.name: getattr(car_obj, column.name) for column in Cars.__table__.columns}
    data['status'] = car_obj.status.name
    return jsonify({'data': data}), 201

@app.route('/cars', methods=['GET'])
def get_cars():
    """
        To get all the car details.
    """
    all_cars = Cars.query.all()
    data = []
    for car in all_cars:
        car_values = {column.name: getattr(car, column.name) for column in Cars.__table__.columns}
        car_values['status'] = car.status.name
        data.append(car_values)
    return jsonify({'data': data}), 200

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    """
        To get the particular car details
        car_id (int) ==> record id
    """
    car_obj = Cars.query.get(car_id)
    if car_obj:
        data = {column.name: getattr(car_obj, column.name) for column in Cars.__table__.columns}
        data['status'] = car_obj.status.name
        return jsonify({'data': data}), 200
    else:
        return jsonify({'message': 'Car not found'}), 404

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_cars(car_id):
    """
        To remove particular car details
        car_id (int) ==> record id
    """
    car_obj = Cars.query.get(car_id)
    if car_obj:
        name = car_obj.model
        db.session.delete(car_obj)
        db.session.commit()
        return jsonify({'message': f'Car {name} deleted successfully'})
    else:
        return jsonify({'error': f'Car not found'}), 404

@app.route('/cars/<int:car_id>', methods=['PUT', 'PATCH'])
def update_cars(car_id):
    """
        To update the car details
    """
    car_obj = Cars.query.get(car_id)
    if not car_obj:
        return jsonify({'error': f'Car not found'}), 404

    data = request.get_json()
    field_names = [column.name for column in Cars.__table__.columns]    
    for key, value in data.items():
        if key == 'status':
            if value == 'booked':
                setattr(car_obj, 'booked_date', datetime.now())
            elif value == 'delivered':
                setattr(car_obj, 'delivered_date', datetime.now())
            elif value == 'cancelled':
                setattr(car_obj, 'cancelled_date', datetime.now())
                setattr(car_obj, 'available', False)
        if hasattr(Cars, key):
            setattr(car_obj, key, value)
    db.session.commit()

    return jsonify({'message': f'Car updated successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)