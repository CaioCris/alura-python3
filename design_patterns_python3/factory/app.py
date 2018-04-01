from design_patterns_python3.factory.connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()

cursor = connection.cursor()
print(cursor)

connection.close()
