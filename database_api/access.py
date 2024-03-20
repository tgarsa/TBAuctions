from utils import database, network#, time

from pandas import DataFrame

# Access to the PostgreSQL database
import psycopg2
from numpy import int64
# from psycopg2.extensions import register_adapter, AsIs
psycopg2.extensions.register_adapter(int64, psycopg2.extensions.AsIs)

# Define the connection
# We won't close because we will need to continued using.
connection = psycopg2.connect(
    host=network.ip,
    port=database.port,
    database=database.database,
    user=database.user,
    password=database.password
)


def get_cuantos(n: int):
    '''
    We recover the last n predictions.
    :param n: Number of predictions to recover
    :return: A dataframe with the n-last predictions.
    '''

    sql = f'select * from predictions order by created_at desc limit {n}'
    # Connect to the database
    cursor = connection.cursor()
    cursor.execute(sql)
    # Recover the data from the cursor
    data = cursor.fetchall()
    # Build the DataFrame to export
    df = DataFrame(data, columns=database.columns)
    cursor.close()
    return df

