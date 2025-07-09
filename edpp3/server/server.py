from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

model_filename = "../public/this_is_not_a_model.pkl"
with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    features = loaded_model.feature_names_in_

    if request.is_json:
        feature_dict = {x: 0 for x in features}
        data = request.get_json()
        hw = 'homeworld_' + data['homeworld']
        ut = 'unit_type_' + data['unitType']

        if hw in feature_dict:
            feature_dict[hw] = 1
        else:
            return jsonify({"error": "invalid homeworld"}), 400

        if ut in feature_dict:
            feature_dict[ut] = 1
        else:
            return jsonify({"error": "invalid unittype"}), 400

        data_df = pd.DataFrame([feature_dict])
        result = loaded_model.predict(data_df)

        result = result.tolist()  # Convert to a list

        return jsonify({"prediction": result[0]})  # Return the result as a JSON response
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
