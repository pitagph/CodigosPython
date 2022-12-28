import mysql.connector
from mysql.connector import errorcode
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except errorcode as err:
        print(f"Error: '{err}'")
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except errorcode as err:
        print(f"Error: '{err}'")
def create_server_connection(host_name, user_name, user_password,database):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=database
        )
        print("MySQL Database connection successful")
    except errorcode as err:
        print(f"Error: '{err}'")
    return connection
conexao = create_server_connection('localhost','root','admin','bancodedados')
# selecionado a tabela
def listardados():
    q1 = """SELECT * FROM produto;"""
    results = read_query(conexao, q1)
    for result in results:
        print(result)
    return results
listardados()