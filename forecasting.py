from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[['day','month','weekday']]
    y = df['sales']

    model = RandomForestRegressor()
    model.fit(X,y)
    return model

def forecast_sales(model, df):
    X = df[['day','month','weekday']]
    df['predicted_sales'] = model.predict(X)
    return df[['date','predicted_sales']]
