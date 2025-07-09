# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import pickle
# import pandas as pd


# app = Flask(__name__)
# CORS(app)

# model_filename = "../public/this_is_not_a_model.pkl"
# with open(model_filename, 'rb') as file:
#     loaded_model = pickle.load(file)



# @app.route('/predict', methods=['POST'])

# def predict():
#     features = ['homeworld_Alderaan', 'homeworld_Aleen Minor', 'homeworld_Bestine IV',
#        'homeworld_Cerea', 'homeworld_Champala', 'homeworld_Chandrila',
#        'homeworld_Concord Dawn', 'homeworld_Corellia', 'homeworld_Dagobah',
#        'homeworld_Dathomir', 'homeworld_Dorin', 'homeworld_Eriadu',
#        'homeworld_Glee Anselm', 'homeworld_Haruun Kal', 'homeworld_Iktotch',
#        'homeworld_Iridonia', 'homeworld_Kalee', 'homeworld_Kashyyyk',
#        'homeworld_Malastare', 'homeworld_Mirial', 'homeworld_Mon Cala',
#        'homeworld_Muunilinst', 'homeworld_Naboo', 'homeworld_Ojom',
#        'homeworld_Quermia', 'homeworld_Rodia', 'homeworld_Ryloth',
#        'homeworld_Serenno', 'homeworld_Shili', 'homeworld_Skako',
#        'homeworld_Socorro', 'homeworld_Stewjon', 'homeworld_Sullust',
#        'homeworld_Tatooine', 'homeworld_Tholoth', 'homeworld_Toydaria',
#        'homeworld_Trandosha', 'homeworld_Troiken', 'homeworld_Tund',
#        'homeworld_Umbara', 'homeworld_Vulpter', 'homeworld_Zolan',
#        'unit_type_at-at', 'unit_type_at-st', 'unit_type_resistance_soldier',
#        'unit_type_stormtrooper', 'unit_type_tie_fighter',
#        'unit_type_tie_silencer', 'unit_type_unknown', 'unit_type_x-wing']
    
    

#     if request.is_json:
#         feature_dict = {x: 0 for x in features}
#         data = request.get_json()
#         hw = 'homeworld_' + data['homeworld']
#         ut = 'unit_type_' + data['unitType']

#         if hw in feature_dict:
#             feature_dict[hw] = 1
#         else:
#             return jsonify({"error": "invalid homeworld"}), 400

#         if ut in feature_dict:
#             feature_dict[ut] = 1
#         else:
#             return jsonify({"error": "invalid unittype"}), 400

        
#         hw = "homeworld_" + data['homeworld']
#         ut = "unit_type_" + data['unitType']
#         # d = {hw: 1, ut: 1}
#         data_df = pd.DataFrame([feature_dict])
#         result = loaded_model.predict(data_df)
#         print(result)

        
#         # return jsonify({"message": "Received data", "data": result}), 200
#         return jsonify(list(result))
#     else:
#         return jsonify({"error": "Request must be JSON"}), 400

# if __name__ == '__main__':
#     app.run(debug=True)

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
    features = ['homeworld_Alderaan', 'homeworld_Aleen Minor', 'homeworld_Bestine IV',
       'homeworld_Cerea', 'homeworld_Champala', 'homeworld_Chandrila',
       'homeworld_Concord Dawn', 'homeworld_Corellia', 'homeworld_Dagobah',
       'homeworld_Dathomir', 'homeworld_Dorin', 'homeworld_Eriadu',
       'homeworld_Glee Anselm', 'homeworld_Haruun Kal', 'homeworld_Iktotch',
       'homeworld_Iridonia', 'homeworld_Kalee', 'homeworld_Kashyyyk',
       'homeworld_Malastare', 'homeworld_Mirial', 'homeworld_Mon Cala',
       'homeworld_Muunilinst', 'homeworld_Naboo', 'homeworld_Ojom',
       'homeworld_Quermia', 'homeworld_Rodia', 'homeworld_Ryloth',
       'homeworld_Serenno', 'homeworld_Shili', 'homeworld_Skako',
       'homeworld_Socorro', 'homeworld_Stewjon', 'homeworld_Sullust',
       'homeworld_Tatooine', 'homeworld_Tholoth', 'homeworld_Toydaria',
       'homeworld_Trandosha', 'homeworld_Troiken', 'homeworld_Tund',
       'homeworld_Umbara', 'homeworld_Vulpter', 'homeworld_Zolan',
       'unit_type_at-at', 'unit_type_at-st', 'unit_type_resistance_soldier',
       'unit_type_stormtrooper', 'unit_type_tie_fighter',
       'unit_type_tie_silencer', 'unit_type_unknown', 'unit_type_x-wing']

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

        # Convert result to a serializable Python type (e.g., int or list)
        # Assuming result is an array-like object (e.g., numpy array)
        result = result.tolist()  # Convert to a list

        return jsonify({"prediction": result[0]})  # Return the result as a JSON response
    else:
        return jsonify({"error": "Request must be JSON"}), 400

if __name__ == '__main__':
    app.run(debug=True)
