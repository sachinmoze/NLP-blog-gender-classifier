from flask import Flask, request, jsonify, render_template
import joblib

# Load the model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            X = vectorizer.transform([text])
            prediction = model.predict(X)[0]
            return render_template('index.html', prediction=prediction, text=text)
    return render_template('index.html', error='No text provided')

if __name__ == '__main__':
    app.run(debug=True)
