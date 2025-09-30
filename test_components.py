"""
Simple tests for the Fake News Detector components
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from text_processor import clean_text, preprocess_text
import joblib

def test_text_processor():
    """Test text processing functions"""
    print("Testing text processor...")
    
    # Test 1: Lowercase conversion
    text = "THIS IS UPPERCASE TEXT"
    result = clean_text(text)
    assert result == "this is uppercase text", f"Expected lowercase, got: {result}"
    print("✓ Lowercase conversion works")
    
    # Test 2: URL removal
    text = "Check this out http://example.com and www.test.com"
    result = clean_text(text)
    assert "http" not in result and "www" not in result, f"URLs not removed: {result}"
    print("✓ URL removal works")
    
    # Test 3: Special characters removal
    text = "Hello!!! This is #awesome @user"
    result = clean_text(text)
    assert "#" not in result and "@" not in result and "!" not in result, f"Special chars not removed: {result}"
    print("✓ Special characters removal works")
    
    # Test 4: Email removal
    text = "Contact me at test@example.com for more info"
    result = clean_text(text)
    assert "@" not in result, f"Email not removed: {result}"
    print("✓ Email removal works")
    
    print("✅ All text processor tests passed!\n")

def test_model_exists():
    """Check if trained model exists"""
    print("Checking model files...")
    
    model_path = "model/fake_news_model.pkl"
    vectorizer_path = "model/vectorizer.pkl"
    
    if os.path.exists(model_path):
        print(f"✓ Model found at {model_path}")
        model = joblib.load(model_path)
        print(f"  Model type: {type(model).__name__}")
    else:
        print(f"✗ Model not found at {model_path}")
        print("  Run: python train_model.py")
        return False
    
    if os.path.exists(vectorizer_path):
        print(f"✓ Vectorizer found at {vectorizer_path}")
        vectorizer = joblib.load(vectorizer_path)
        print(f"  Vectorizer type: {type(vectorizer).__name__}")
    else:
        print(f"✗ Vectorizer not found at {vectorizer_path}")
        return False
    
    print("✅ Model files OK!\n")
    return True

def test_prediction():
    """Test model prediction"""
    print("Testing model prediction...")
    
    if not os.path.exists("model/fake_news_model.pkl"):
        print("⚠️  Model not trained. Skipping prediction test.")
        return
    
    model = joblib.load("model/fake_news_model.pkl")
    vectorizer = joblib.load("model/vectorizer.pkl")
    
    # Test fake news
    fake_text = "Scientists confirm aliens built pyramids using secret technology"
    fake_cleaned = preprocess_text(fake_text)
    fake_vectorized = vectorizer.transform([fake_cleaned])
    fake_prediction = model.predict(fake_vectorized)[0]
    fake_proba = model.predict_proba(fake_vectorized)[0]
    
    print(f"Test 1 - Fake news:")
    print(f"  Text: {fake_text[:50]}...")
    print(f"  Prediction: {'Fake' if fake_prediction == 1 else 'Real'}")
    print(f"  Confidence: {max(fake_proba) * 100:.2f}%")
    
    # Test real news
    real_text = "Scientists publish peer-reviewed study on climate change impacts"
    real_cleaned = preprocess_text(real_text)
    real_vectorized = vectorizer.transform([real_cleaned])
    real_prediction = model.predict(real_vectorized)[0]
    real_proba = model.predict_proba(real_vectorized)[0]
    
    print(f"\nTest 2 - Real news:")
    print(f"  Text: {real_text[:50]}...")
    print(f"  Prediction: {'Fake' if real_prediction == 1 else 'Real'}")
    print(f"  Confidence: {max(real_proba) * 100:.2f}%")
    
    print("\n✅ Prediction tests completed!\n")

if __name__ == "__main__":
    print("=" * 60)
    print("Fake News Detector - Component Tests")
    print("=" * 60)
    print()
    
    try:
        test_text_processor()
        test_model_exists()
        test_prediction()
        
        print("=" * 60)
        print("✅ All tests completed successfully!")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
