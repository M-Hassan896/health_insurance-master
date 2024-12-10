from flask import Flask, render_template, request
import pickle
import numpy as np
from flask import flash, redirect, url_for

# Flask app setup
app = Flask(__name__)

app.secret_key = 'supersecretkey'  # Required for flashing messages

# Load the model
model_filename = "E:/health_insurance-fyp/health_insurance-fyp/health_insurance-master/random_forest_model.pkl"

with open(model_filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Home route to render the form
@app.route('/', methods=['GET'])
def Home():
    return render_template('home.html')

# Prediction route to handle form submission and render the result
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract form data
        age = float(request.form['age'])
        sex = int(request.form['sex'])  # 1 for Male, 0 for Female
        smoker = int(request.form['smoker'])  # 1 for Smoker, 0 for Non-smoker
        bmi = float(request.form['bmi'])  # Body Mass Index
        children = int(request.form['children'])
        region = int(request.form['region'])  # Region represented as an integer

        # Create the input array
        input_array = np.array([[age, sex, smoker, bmi, children, region]])

        # Predict and round the result
        prediction = loaded_model.predict(input_array)
        predicted_value = round(prediction[0], 2)

        # Render the result template with the prediction
        return render_template('result.html', prediction_text=f'Estimated medical insurance cost is {predicted_value}')
# Home route to render the form
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Here you would add authentication logic
        flash('Login successful!')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        flash('Signup successful!')
        return redirect(url_for('Signup'))
    return render_template('signup.html')

@app.route('/Contactus', methods=['GET', 'POST'])
def Contactus():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Here you would typically process the contact form data
        flash('Your message has been sent successfully!')
        return redirect(url_for('Contactus'))
    return render_template('contactus.html')


@app.route('/Aboutus', methods=['GET'])
def Aboutus():
    return render_template('Aboutus.html')

@app.route('/models', methods=['GET'])
def models():
    return render_template('models.html')

if __name__ == "__main__":
    app.run(debug=True)
