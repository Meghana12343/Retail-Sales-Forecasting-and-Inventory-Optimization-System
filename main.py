from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.forecasting import train_model, forecast_sales
from src.inventory import inventory_optimization
from src.visualization import plot_forecast

def main():
    df = load_data("data/raw/sales_data.csv")
    df = clean_data(df)
    df = create_features(df)

    model = train_model(df)
    forecast = forecast_sales(model, df)

    inventory = inventory_optimization(forecast)

    plot_forecast(df, forecast)

    forecast.to_csv("outputs/forecast.csv", index=False)
    inventory.to_csv("outputs/inventory.csv", index=False)

if __name__ == "__main__":
    main()
