from http.client import responses
from http.client import responses
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/classify_image', methods = ['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python flask server for sport celebity image classification.")
    util.load_saved_artifacts()

    app.run(port = 5000)