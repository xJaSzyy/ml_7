from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':
    print("Hello, world")
    app.run(host='0.0.0.0', port=5000)
