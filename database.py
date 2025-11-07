"""
Database module for 3D Model Viewer
Handles SQLite database operations for model storage
"""
import sqlite3
import os
from datetime import datetime

DATABASE_PATH = 'models.db'

def init_db():
    """Initialize the database with required tables"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS models (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            original_filename TEXT NOT NULL,
            file_path TEXT NOT NULL,
            upload_date TEXT NOT NULL,
            user_id TEXT DEFAULT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database initialized successfully")

def add_model(filename, original_filename, file_path, user_id=None):
    """
    Add a new model to the database
    
    Args:
        filename (str): Stored filename
        original_filename (str): Original uploaded filename
        file_path (str): Path to the stored file
        user_id (str): Optional user identifier
        
    Returns:
        int: ID of the inserted model
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    upload_date = datetime.now().isoformat()
    
    cursor.execute('''
        INSERT INTO models (filename, original_filename, file_path, upload_date, user_id)
        VALUES (?, ?, ?, ?, ?)
    ''', (filename, original_filename, file_path, upload_date, user_id))
    
    model_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return model_id

def get_model(model_id):
    """
    Get model information by ID
    
    Args:
        model_id (int): Model ID
        
    Returns:
        dict: Model information or None if not found
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM models WHERE id = ?', (model_id,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return dict(row)
    return None

def get_all_models():
    """
    Get all models from the database
    
    Returns:
        list: List of model dictionaries
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM models ORDER BY upload_date DESC')
    rows = cursor.fetchall()
    conn.close()
    
    return [dict(row) for row in rows]

def delete_model(model_id):
    """
    Delete a model from the database
    
    Args:
        model_id (int): Model ID
        
    Returns:
        bool: True if deleted, False if not found
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM models WHERE id = ?', (model_id,))
    deleted = cursor.rowcount > 0
    
    conn.commit()
    conn.close()
    
    return deleted
