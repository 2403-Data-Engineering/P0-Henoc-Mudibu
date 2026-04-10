import os
import mysql.connector

from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()



class DBConnection:

    @staticmethod
    def get_connection():
        try:
            return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("PORT", 3306)),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASS"),
            database=os.getenv("DB_NAME")
            )
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None
    

#     def test_connection() -> None:
#         with DBConnection.get_connection() as conn:
#             cursor = conn.cursor(dictionary=True)

#             sql = "CREATE TABLE test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255))"

#             cursor.execute(sql)

# DBConnection.test_connection()
