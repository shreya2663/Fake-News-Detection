from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the Decision Tree model
with open('model.pkl', 'rb') as f:
    newmodel = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        input_data = request.form['text']
    
    # Preprocess the input text if necessary
    
    # Make predictions using the loaded model
    prediction = newmodel.predict([input_data])
    
    # Prepare the response
    if prediction == 'fake':
        result = 'Fake News'
    else:
        result = 'Real News'
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run()
