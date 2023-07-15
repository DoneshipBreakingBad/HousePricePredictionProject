from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)
data = pd.read_csv('cleaned data.csv')
pipe = pickle.load(open("ridge_model.pkl", 'rb'))


@app.route('/')
def index():
    cities = sorted(data['city'].unique())
    return render_template('index.html', cities=cities)


@app.route('/predict', methods=['POST'])
def predict():
    city = request.form.get('city')
    bhk = request.form.get('bhk')
    size = float(request.form.get('size'))

    print(city, bhk, size)
    input = pd.DataFrame([[city, bhk, size]], columns=['city', 'BHK', 'size_sqft'])
    prediction = pipe.predict(input)[0] * 1e5

    return str(np.round(prediction, 2))


if __name__ == '__main__':
    app.run(debug=True, port=5001)