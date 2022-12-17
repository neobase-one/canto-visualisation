import psycopg2
from sqlalchemy import create_engine
import os

def get_db_connection():
    DB_URI = os.getenv("DB_URI")
    connection = create_engine(DB_URI)
    return connection