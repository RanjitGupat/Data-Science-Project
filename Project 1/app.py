import pickle
import numpy as np
from flask import Flask, request, render_template

app = Flask(__name__)

# model load
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])

        features = np.array([[cgpa, iq]])

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "Placement Hoga"
        else:
            result = "Placement Nahi Hoga"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text="Error: " + str(e))


if __name__ == "__main__":
    app.run(debug=True)