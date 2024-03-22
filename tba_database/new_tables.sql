
-- CREATE TABLE Predictions.

DROP TABLE IF EXISTS predictions;
CREATE TABLE predictions (
       id SERIAL PRIMARY KEY,
       item_id INTEGER NOT NULL,
       auction_type INTEGER NOT NULL,
       bid_value REAL NOT NULL,
       bid_time REAL NOT NULL,
       bidder_rate REAL NOT NULL,
       open_price REAL NOT NULL,
       rank INTEGER NOT NULL,
       num_bids INTEGER NOT NULL,
       prev_bid_value REAL NOT NULL,
       prev_bid_value_avg REAL NOT NULL,
       bid_value_delta  REAL NOT NULL,
       prediction REAL NOT NULL,
       model_version VARCHAR NOT NULL,
       created_at TIMESTAMP NOT NULL
);

