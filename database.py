# Created by Ryan Polasky - 5/1/25

import os
import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

# Database connection parameters
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "healthcare")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")


# Context manager for database connections
@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        yield conn
    finally:
        if conn is not None:
            conn.close()


# Context manager for database cursor
@contextmanager
def get_db_cursor():
    with get_db_connection() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor
            conn.commit()
        except Exception:
            conn.rollback()
            raise
        finally:
            cursor.close()


# Helper function to execute queries safely
def execute_query(query, params=None):
    with get_db_cursor() as cursor:
        cursor.execute(query, params)
        try:
            return cursor.fetchall()
        except psycopg2.ProgrammingError:
            # If no results to fetch (for INSERT, UPDATE, DELETE)
            return None


# Helper function to execute a single-row query
def execute_query_single_row(query, params=None):
    with get_db_cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchone()
