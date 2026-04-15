import matplotlib.pyplot as plt

def plot_forecast(df, forecast):
    plt.figure()
    plt.plot(df['date'], df['sales'], label='Actual')
    plt.plot(forecast['date'], forecast['predicted_sales'], label='Forecast')
    plt.legend()
    plt.show()
