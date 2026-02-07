import mysql.connector
import json

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="causal_chat"
    )

def save_turn(query, category, output, remarks=None):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO conversation_log
        (Query, Query_Category, System_Output, Remarks)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            query,
            category,
            json.dumps(output),
            remarks
        ))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Database error: {e}")

def fetch_last_n_turns(n=3):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("""
            SELECT * FROM conversation_log
            ORDER BY Query_Id DESC
            LIMIT %s
        """, (n,))

        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows[::-1]  # chronological order
    except Exception as e:
        print(f"Database error: {e}")
        return []
