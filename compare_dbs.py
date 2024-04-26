import sqlite3
import cx_Oracle

class DatabaseConnector:
    def __init__(self, host, port, service_name, user, password):
        # cx_Oracle.init_oracle_client(lib_dir='drivers')
        dsn = cx_Oracle.makedsn(host, port, service_name)
        self.connection = cx_Oracle.connect(
            user=user,
            password=password,
            dsn=dsn
        )

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        return cursor

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

    def fetch_data_from_view(self, view_name, columns=None, condition=None):
        if columns:
            columns_str = ', '.join(columns)
        else:
            columns_str = '*'
        if condition:
            query = f"SELECT {columns_str} FROM {view_name} WHERE {condition}"
        else:
            query = f"SELECT {columns_str} FROM {view_name}"
        return self.cursor.execute(query).fetchall()

    def create_temp_table_from_oracle_view(self, oracle_connection_string, view_name, temp_table_name):
        oracle_conn = cx_Oracle.connect(oracle_connection_string)
        oracle_cursor = oracle_conn.cursor()
        oracle_cursor.execute(f"SELECT * FROM {view_name}")
        columns = [desc[0] for desc in oracle_cursor.description]
        self.create_table(temp_table_name, columns)
        for row in oracle_cursor:
            self.insert_data(temp_table_name, row)
        oracle_cursor.close()
        oracle_conn.close()

    def compare_data(self, oracle_connection_string, view_name, temp_table_name):
        self.create_temp_table_from_oracle_view(oracle_connection_string, view_name, temp_table_name)
        oracle_data = self.fetch_data_from_view(view_name)
        sqlite_data = self.fetch_data(temp_table_name)
        new_values = [data for data in oracle_data if data not in sqlite_data]
        return new_values

    def close_connection(self):
        self.conn.close()

# Exemplo de uso:
db = SQLiteDB('exemplo.db')

# Criar uma tabela temporária com dados da view Oracle
oracle_connection_string = 'username/password@hostname:port/service_name'
view_name = 'nome_da_sua_view'
temp_table_name = 'temp_data'
db.create_temp_table_from_oracle_view(oracle_connection_string, view_name, temp_table_name)

# Comparar os dados da view Oracle com os dados na tabela temporária
novos_valores = db.compare_data(oracle_connection_string, view_name, temp_table_name)
print("Novos valores na view Oracle:", novos_valores)

# Fechar conexão com o banco de dados
db.close_connection()
