from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (you can replace this with your own data source)
data = {
    "1": {"name": "John", "age": 30, "city": "New York"},
    "2": {"name": "Alice", "age": 25, "city": "Los Angeles"},
    "3": {"name": "Bob", "age": 35, "city": "Chicago"}
}

# GET request to retrieve all data
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

# GET request to retrieve data by ID
@app.route('/api/data/<id>', methods=['GET'])
def get_data_by_id(id):
    if id in data:
        return jsonify(data[id])
    else:
        return jsonify({"error": "Data not found"}), 404

# POST request to add new data
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.json
    data[str(len(data) + 1)] = new_data
    return jsonify({"message": "Data added successfully"}), 201

# PUT request to update existing data
@app.route('/api/data/<id>', methods=['PUT'])
def update_data(id):
    if id in data:
        data[id] = request.json
        return jsonify({"message": "Data updated successfully"})
    else:
        return jsonify({"error": "Data not found"}), 404

# DELETE request to delete data by ID
@app.route('/api/data/<id>', methods=['DELETE'])
def delete_data(id):
    if id in data:
        del data[id]
        return jsonify({"message": "Data deleted successfully"})
    else:
        return jsonify({"error": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
