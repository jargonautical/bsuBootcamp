# Import necessary modules
import numpy as np
from flask import Flask, request, render_template, jsonify
import pickle
 
# Initialise Flask app and load the model
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

# Define home route and its corresponding request handler
@app.route('/')
def home():
    return render_template('index.html')

# Define predict route for rendering results on HTML GUI
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='Salary is {}'.format(output))

# Define predict_api route for making predictions through API calls
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
