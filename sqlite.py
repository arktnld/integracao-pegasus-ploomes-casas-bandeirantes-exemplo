import sqlite3

class SQLiteDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})")
        self.conn.commit()

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data))])
        self.cursor.execute(f"INSERT INTO {table_name} VALUES ({placeholders})", data)
        self.conn.commit()

    def fetch_data(self, table_name, condition=None):
        if condition:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {condition}")
        else:
            self.cursor.execute(f"SELECT * FROM {table_name}")
        return self.cursor.fetchall()

    def value_exists(self, table_name, column_name, value):
        self.cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name}=?", (value,))
        count = self.cursor.fetchone()[0]
        return count > 0

    def close_connection(self):
        self.conn.close()
