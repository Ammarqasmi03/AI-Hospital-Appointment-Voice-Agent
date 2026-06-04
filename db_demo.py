from __future__ import annotations

from sqlalchemy import text

from database import engine, init_db

def run_query(query: str):
    """Run a SQL query on the same DB used by database.py.
    
    Example : 
           rows = run_sql("SELECT * FROM appointments")
           for row in rows:
               print(row)
               
    """

    with engine.begin() as connection:
        result = connection.execute(text(query))
        return result.fetchall() if result.returns_rows else result.rowcount
    
query = """Insert INTO appointments (patient_name, reason, doctor_name, date, start_time) VALUES ('John Doe', 'Checkup', 'Dr. Smith', '2024-07-01', '10:00:00')"""
query1 = """SELECT * FROM appointments"""
query2 = """DELETE FROM appointments WHERE patient_name = 'John Doe'"""
print(run_query(query))
print(run_query(query1))
print(run_query(query2))