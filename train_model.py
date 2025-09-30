"""
Train a simple fake news detection model
Uses a publicly available dataset and trains a Logistic Regression model
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os
from text_processor import preprocess_text

def create_sample_dataset():
    """
    Create a sample dataset for demonstration purposes
    In a real scenario, you would load a dataset from Kaggle or another source
    """
    # Sample fake news articles
    fake_articles = [
        "Scientists confirm aliens built pyramids using secret technology",
        "Government hiding cure for all diseases from public",
        "Celebrity caught doing something completely unbelievable",
        "Miracle cure discovered by single doctor cures everything",
        "Secret conspiracy revealed by anonymous insider",
        "Shocking truth about world leaders revealed",
        "Ancient prophecy predicts end of world next week",
        "Mysterious object found proves everything we know is wrong",
        "Celebrity scandal that will shock you",
        "Government admits to covering up alien contact",
        "New study proves impossible thing is actually true",
        "Breaking: Famous person does unbelievable thing",
        "Scientists baffled by mysterious phenomenon",
        "Ancient civilization had advanced technology we can't explain",
        "Secret documents reveal shocking truth about everything",
    ]
    
    # Sample real news articles
    real_articles = [
        "Scientists publish peer-reviewed study on climate change impacts",
        "Economic indicators show moderate growth in third quarter",
        "Government announces new infrastructure spending plan",
        "Research team makes progress on renewable energy efficiency",
        "Local community organizes charity event for hospital",
        "Technology company reports quarterly earnings results",
        "International summit addresses global trade policies",
        "University researchers develop new medical treatment protocol",
        "City council approves budget for public transportation improvements",
        "Sports team wins championship in overtime game",
        "Educational institution receives accreditation renewal",
        "Weather service issues forecast for upcoming week",
        "Company announces plans to expand operations and hire staff",
        "Museum opens new exhibition featuring historical artifacts",
        "Agricultural report shows crop yields meet expectations",
    ]
    
    # Create DataFrame
    df = pd.DataFrame({
        'text': fake_articles + real_articles,
        'label': [1] * len(fake_articles) + [0] * len(real_articles)  # 1 = fake, 0 = real
    })
    
    return df

def train_model(use_sample_data=True):
    """
    Train the fake news detection model
    
    Args:
        use_sample_data (bool): If True, uses sample data. Otherwise, load from file.
    """
    print("Loading dataset...")
    
    if use_sample_data:
        df = create_sample_dataset()
        print(f"Created sample dataset with {len(df)} articles")
    else:
        # In a real scenario, load dataset from file
        # df = pd.read_csv('fake_news_dataset.csv')
        print("Note: Using sample data. For better results, use a real dataset.")
        df = create_sample_dataset()
    
    print(f"Dataset size: {len(df)} articles")
    print(f"Fake news: {sum(df['label'] == 1)}, Real news: {sum(df['label'] == 0)}")
    
    # Preprocess text
    print("\nPreprocessing text...")
    df['cleaned_text'] = df['text'].apply(preprocess_text)
    
    # Split data
    X = df['cleaned_text']
    y = df['label']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print(f"Training set: {len(X_train)}, Test set: {len(X_test)}")
    
    # Create TF-IDF vectorizer
    print("\nCreating TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer(
        max_features=5000,
        min_df=1,
        max_df=0.8,
        ngram_range=(1, 2)
    )
    
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)
    
    # Train Logistic Regression model
    print("\nTraining Logistic Regression model...")
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_vectorized, y_train)
    
    # Evaluate model
    print("\nEvaluating model...")
    y_pred = model.predict(X_test_vectorized)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy: {accuracy * 100:.2f}%")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Real', 'Fake']))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    # Save model and vectorizer
    print("\nSaving model and vectorizer...")
    os.makedirs('model', exist_ok=True)
    joblib.dump(model, 'model/fake_news_model.pkl')
    joblib.dump(vectorizer, 'model/vectorizer.pkl')
    
    print("Model and vectorizer saved successfully!")
    print("\nModel training complete. You can now run the web application with: python app.py")

if __name__ == '__main__':
    train_model(use_sample_data=True)
