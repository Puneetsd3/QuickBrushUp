import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="day1test",
        user="postgres",
        password="postgres",
        host="localhost"
    )