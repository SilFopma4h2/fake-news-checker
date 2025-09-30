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
import argparse
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

def load_csv_dataset(csv_path, text_column=None, label_column=None):
    """
    Load dataset from CSV file (e.g., from Kaggle)
    
    Args:
        csv_path (str): Path to CSV file
        text_column (str): Name of the column containing text. If None, tries common names.
        label_column (str): Name of the column containing labels. If None, tries common names.
    
    Returns:
        pd.DataFrame: DataFrame with 'text' and 'label' columns
    """
    print(f"Loading dataset from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    print(f"CSV loaded. Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Auto-detect text column if not specified
    if text_column is None:
        common_text_cols = ['text', 'title', 'article', 'content', 'news', 'statement', 'claim']
        for col in common_text_cols:
            if col in df.columns:
                text_column = col
                print(f"Auto-detected text column: '{text_column}'")
                break
        if text_column is None:
            raise ValueError(f"Could not auto-detect text column. Please specify with --text-column. Available columns: {list(df.columns)}")
    
    # Auto-detect label column if not specified
    if label_column is None:
        common_label_cols = ['label', 'target', 'class', 'category', 'is_fake', 'fake']
        for col in common_label_cols:
            if col in df.columns:
                label_column = col
                print(f"Auto-detected label column: '{label_column}'")
                break
        if label_column is None:
            raise ValueError(f"Could not auto-detect label column. Please specify with --label-column. Available columns: {list(df.columns)}")
    
    # Validate columns exist
    if text_column not in df.columns:
        raise ValueError(f"Text column '{text_column}' not found in CSV. Available columns: {list(df.columns)}")
    if label_column not in df.columns:
        raise ValueError(f"Label column '{label_column}' not found in CSV. Available columns: {list(df.columns)}")
    
    # Create standardized DataFrame
    result_df = pd.DataFrame({
        'text': df[text_column],
        'label': df[label_column]
    })
    
    # Remove rows with missing values
    result_df = result_df.dropna()
    
    # Ensure labels are binary (0 or 1)
    unique_labels = result_df['label'].unique()
    print(f"Unique labels in dataset: {unique_labels}")
    
    # Convert labels to binary if needed
    if set(unique_labels).issubset({0, 1}):
        # Already binary, no mapping needed
        print("Labels are already binary (0 and 1)")
    elif len(unique_labels) == 2:
        # Map to 0 and 1 (first unique label -> 0, second -> 1)
        label_mapping = {unique_labels[0]: 0, unique_labels[1]: 1}
        result_df['label'] = result_df['label'].map(label_mapping)
        print(f"Label mapping applied: {label_mapping}")
    else:
        raise ValueError(f"Expected 2 unique labels, found {len(unique_labels)}: {unique_labels}")
    
    print(f"Dataset loaded successfully. {len(result_df)} rows after removing NaN values.")
    
    return result_df

def train_model(csv_path=None, text_column=None, label_column=None, use_sample_data=False):
    """
    Train the fake news detection model
    
    Args:
        csv_path (str): Path to CSV file. If provided, loads data from CSV.
        text_column (str): Name of the column containing text in CSV.
        label_column (str): Name of the column containing labels in CSV.
        use_sample_data (bool): If True, uses sample data. Ignored if csv_path is provided.
    """
    print("Loading dataset...")
    
    if csv_path:
        df = load_csv_dataset(csv_path, text_column, label_column)
        print(f"Loaded dataset from CSV: {len(df)} articles")
    elif use_sample_data:
        df = create_sample_dataset()
        print(f"Created sample dataset with {len(df)} articles")
    else:
        print("No CSV path provided and use_sample_data is False.")
        print("Using sample data. For better results, provide a CSV file with --csv option.")
        df = create_sample_dataset()
        print(f"Created sample dataset with {len(df)} articles")
    
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
    parser = argparse.ArgumentParser(description='Train fake news detection model')
    parser.add_argument('--csv', type=str, help='Path to CSV file containing the dataset')
    parser.add_argument('--text-column', type=str, help='Name of the column containing text (auto-detected if not specified)')
    parser.add_argument('--label-column', type=str, help='Name of the column containing labels (auto-detected if not specified)')
    parser.add_argument('--sample', action='store_true', help='Use sample data instead of CSV')
    
    args = parser.parse_args()
    
    train_model(
        csv_path=args.csv,
        text_column=args.text_column,
        label_column=args.label_column,
        use_sample_data=args.sample
    )

