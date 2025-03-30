import sqlite3
import os
from cryptography.fernet import Fernet
from datetime import datetime

# Caminho do banco e da chave
DB_PATH = os.path.join("secure_logs", "logs.db")
KEY_PATH = os.path.join("secure_logs", "key.key")

# Gera a chave se não existir
def generate_key():
    if not os.path.exists(KEY_PATH):
        key = Fernet.generate_key()
        with open(KEY_PATH, 'wb') as f:
            f.write(key)

def load_key():
    with open(KEY_PATH, 'rb') as f:
        return f.read()

# Inicializa o banco
def init_db():
    generate_key()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            filename TEXT,
            label TEXT,
            confidence TEXT,
            hash_val TEXT,
            hash_match TEXT,
            encrypted_data BLOB
        )
    ''')
    conn.commit()
    conn.close()

# Insere log criptografado
def save_log(filename, label, confidence, hash_val, hash_match):
    key = load_key()
    fernet = Fernet(key)
    
    raw_data = f"File: {filename} | Label: {label} | Confidence: {confidence}% | Hash: {hash_val} | Match: {hash_match}"
    encrypted = fernet.encrypt(raw_data.encode())

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (timestamp, filename, label, confidence, hash_val, hash_match, encrypted_data)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        datetime.now().isoformat(),
        filename,
        label,
        f"{confidence}%",
        hash_val,
        "Yes" if hash_match else "No",
        encrypted
    ))
    conn.commit()
    conn.close()
