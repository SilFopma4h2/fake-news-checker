"""
Text preprocessing module for fake news detection
Handles text cleaning and preparation for model training and prediction
"""
import re
import string

def clean_text(text):
    """
    Clean and preprocess text for analysis
    
    Args:
        text (str): Raw text input
        
    Returns:
        str: Cleaned text
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and digits (but keep spaces)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

def preprocess_text(text):
    """
    Full preprocessing pipeline
    
    Args:
        text (str): Raw text input
        
    Returns:
        str: Preprocessed text ready for vectorization
    """
    return clean_text(text)
