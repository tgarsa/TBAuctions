# The necessary imports
import xgboost as xgb
from sklearn.model_selection import KFold


def get_prediction(df):
    model = xgb.XGBRegressor()
    model.load_model('xgb.json')
    predict = model.predict(df)
    return predict


def train_model(df):
    X = df.drop(columns=['closing_price'], axis=1)
    y = df['closing_price']
    # kf = KFold(n_splits=5,
    #            shuffle=True,
    #            random_state=42)
    booster = xgb.XGBRegressor(tree_method="approx",
                               enable_categorical=True,
                               eta=0.03,
                               max_depth=11,
                               n_estimators=250,
                               subsample=0.5)
    model = booster.fit(X, y)
    model.save_model('xgb.json')
    return 'Done It'

