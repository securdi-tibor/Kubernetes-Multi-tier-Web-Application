from flask import Flask, jsonify
import psycopg2
import os
from datetime import datetime

app = Flask(__name__)

# Database connection function
def get_db_connection():
    try:
        connection = psycopg2.connect(
            host=os.environ.get('DB_HOST', 'pg-service'),
            database=os.environ.get('POSTGRES_DB', 'myapp'),
            user=os.environ.get('POSTGRES_USER', 'postgres'),
            password=os.environ.get('POSTGRES_PASSWORD', 'password123'),
            port=os.environ.get('DB_PORT', '5432')
        )
        return connection
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'flask-backend'
    })

# Database test endpoint
@app.route('/db-test')
def db_test():
    conn = get_db_connection()
    if conn is None:
        return jsonify({
            'status': 'error',
            'message': 'Database connection failed'
        }), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return jsonify({
            'status': 'success',
            'message': 'Database connection successful',
            'postgres_version': version[0] if version else 'Unknown'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Database query failed: {str(e)}'
        }), 500

# Main endpoint
@app.route('/')
def home():
    return jsonify({
        'message': 'Welcome to the Multi-Tier Web Application Backend!',
        'endpoints': {
            'health': '/health',
            'db_test': '/db-test'
        },
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
