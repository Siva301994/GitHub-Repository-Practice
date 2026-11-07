import mysql.connector
from mysql.connector import Error

def main():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Siva@524407",
            database="mydb"
        )
        if conn.is_connected():
            print("Connected to MySQL db 'mydb'")
            cur = conn.cursor()
            cur.execute("SELECT * FROM test;")
            rows = cur.fetchall()
            if rows:
                print(f"Fetched {len(rows)} row(s):")
                for r in rows:
                    print(r)
            else:
                print("No rows returned in table `test`.")
    except Error as e:
        print("Error:", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()