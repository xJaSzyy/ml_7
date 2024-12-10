import pickle
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, title="ML API", description="API для работы с моделью машинного обучения")

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

predict_model = api.model('Prediction', {
    'features': fields.List(fields.List(fields.Float, required=True), description="Список списков с признаками")
})


@api.route('/predict')
class Predict(Resource):
    @api.expect(predict_model)
    def post(self):
        """
        Сделать прогноз на основе модели
        """
        data = request.get_json()
        predictions = model.predict(data['features'])
        return jsonify({"predictions": predictions.tolist()})


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    print("Hello, world")
    app.run(host='0.0.0.0', port=5000)
