from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db_connection():
    engine = db.get_engine()
    connection = engine.raw_connection()
    return connection
