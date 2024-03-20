from utils import database, network, time, version

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


def load_predictions(df):
    '''
    We load in the database our predictions.
    :param df: The original data + the prediction
    :return: None
    '''

    # Add the version of the Model, and when we load the predictions
    df['created_at'] = time.now()
    # print('Tomasada')
    # print(time.now())
    df['model_version'] = version
    # SQL to insert the data
    sql = ("INSERT INTO predictions (item_id, auction_type, bid_value, bid_time, bidder_rate, open_price, rank, "
           "num_bids, prev_bid_value, prev_bid_value_avg, bid_value_delta, prediction, model_version, created_at) "
           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    # sql = ("INSERT INTO predictions (item_id, auction_type, bid_value, bid_time, bidder_rate, open_price, rank, "
    #        "num_bids, prev_bid_value, prev_bid_value_avg, bid_value_delta, model_version, created_at) "
    #        "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    # Connect to the database
    cursor = connection.cursor()
    for cont in range(df.shape[0]):
        data = df.iloc[cont]
        print(data)
        cursor.execute(sql, (data['item_id'], data['auction_type'], data['bid_value'], data['bid_time'],
                             data['bidder_rate'], data['open_price'], data['rank'], data['num_bids'],
                             data['prev_bid_value'], data['prev_bid_value_avg'], data['bid_value_delta'],
                             data['prediction'], data['model_version'], data['created_at']))

        # cursor.execute(sql, (data['item_id'], data['auction_type'], data['bid_value'], data['bid_time'],
        #                      data['bidder_rate'], data['open_price'], data['rank'], data['num_bids'],
        #                      data['prev_bid_value'], data['prev_bid_value_avg'], data['bid_value_delta'],
        #                      data['model_version'], data['created_at']))

        connection.commit()
    cursor.close()

