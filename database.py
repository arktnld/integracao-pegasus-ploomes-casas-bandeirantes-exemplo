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

class DataProcessor:
    @staticmethod
    def process_row(row):
        # Process the row here
        # You can add more processing logic as needed
        return {
            "nomefantasia": row[0],
            "razaosocial": row[1],
            "cnpj": row[2],
            "cnae": row[3],
            "cep": row[4],
            "endereco": row[5],
            "bairro": row[7],
            "estado": row[8],
            "cidade": row[9],
            "telefone": row[11],
            "email": row[12],
            "vendedor": row[13],
            "promotor": row[14],
            "classificacaopessoa": row[15]
        }

class DataPrinter:
    @staticmethod
    def print_data(data):
        for key, value in data.items():
            print(f"{key}: {value}")

# def main():
#     oracle = DatabaseConnector(
#         host='192.168.0.7',
#         port=1521,
#         service_name='ora11g',
#         user='crm',
#         password='cb4nd1520'
#     )

#     cursor = oracle.execute_query(config.query)

#     for row in cursor:
#         processed_data = DataProcessor.process_row(row)
#         DataPrinter.print_data(processed_data)

#     oracle.close()

# if __name__ == "__main__":
#     main()
