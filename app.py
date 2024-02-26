from flask import Flask, render_template, request, jsonify
from utils import predict_drug_type

app = Flask(__name__)

# API for categorical column "Sex"
@app.route('/api/sex', methods=['GET'])
def sex_api():
    sex_values = ['M', 'F']
    return jsonify(sex_values)

# API for categorical column "BP"
@app.route('/api/bp', methods=['GET'])
def bp_api():
    bp_values = ['LOW', 'HIGH', 'NORMAL']
    return jsonify(bp_values)

# API for categorical column "Cholesterol"
@app.route('/api/cholesterol', methods=['GET'])
def cholesterol_api():
    cholesterol_values = ['HIGH', 'NORMAL']
    return jsonify(cholesterol_values)

# Prediction API
@app.route('/api/predict', methods=['POST'])
def predict_api():
    data = request.get_json()

    age = int(data['age'])
    sex = int(data['sex'])
    bp = int(data['bp'])
    cholesterol = int(data['cholesterol'])
    Na_to_K = float(data['na_to_z'])
    
    predicted_drug = predict_drug_type(age, Na_to_K, sex, bp, cholesterol)

    return jsonify({'predicted_drug': predicted_drug})

# Homepage API
@app.route('/')
def homepage():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)
