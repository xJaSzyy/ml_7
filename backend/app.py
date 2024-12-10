import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    predictions = model.predict(data['features'])
    return jsonify({"predictions": predictions.tolist()})


if __name__ == '__main__':
    print("Hello, world")
    app.run(host='0.0.0.0', port=5000)
