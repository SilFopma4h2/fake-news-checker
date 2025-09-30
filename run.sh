#!/bin/bash
# Fake News Detector - Easy Run Script

echo "🔍 Fake News Detector - MVP"
echo "=============================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if requirements are installed
echo ""
echo "📦 Checking dependencies..."
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Dependencies not installed. Installing now..."
    pip install -r requirements.txt
fi

# Check if model exists
if [ ! -f "model/fake_news_model.pkl" ]; then
    echo ""
    echo "⚠️  Model not found. Training model..."
    python3 train_model.py
fi

echo ""
echo "🚀 Starting web application..."
echo ""
echo "📍 Open your browser and go to: http://localhost:5001"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
