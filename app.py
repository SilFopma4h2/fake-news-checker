"""
Fake News Detector - MVP
A simple web application that analyzes news articles and predicts if they are fake or real.
"""
from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the trained model and vectorizer
MODEL_PATH = 'model/fake_news_model.pkl'
VECTORIZER_PATH = 'model/vectorizer.pkl'

model = None
vectorizer = None

def load_model():
    """Load the trained model and vectorizer"""
    global model, vectorizer
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return True
    return False

@app.route('/')
def index():
    """Main page with input form"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Predict if the news article is fake or real"""
    try:
        # Get the article text from the request
        data = request.get_json()
        article_text = data.get('text', '').strip()
        
        if not article_text:
            return jsonify({
                'error': 'Geen tekst ingevoerd. Voer een nieuwsartikel in.'
            }), 400
        
        # Check if model is loaded
        if model is None or vectorizer is None:
            if not load_model():
                return jsonify({
                    'error': 'Model nog niet getraind. Run eerst train_model.py'
                }), 500
        
        # Vectorize the input text
        text_vectorized = vectorizer.transform([article_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)[0]
        
        # Get confidence score (probability)
        probabilities = model.predict_proba(text_vectorized)[0]
        confidence = max(probabilities) * 100
        
        # Determine result
        result = 'Fake' if prediction == 1 else 'Real'
        
        return jsonify({
            'result': result,
            'confidence': round(confidence, 2),
            'message': f'Dit artikel is waarschijnlijk {result.lower()} news.'
        })
        
    except Exception as e:
        return jsonify({
            'error': f'Er is een fout opgetreden: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Try to load model on startup
    load_model()
    app.run(debug=True, host='0.0.0.0', port=5001)
