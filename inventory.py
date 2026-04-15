def inventory_optimization(forecast):
    forecast['safety_stock'] = forecast['predicted_sales'] * 0.2
    forecast['reorder_point'] = forecast['predicted_sales'] + forecast['safety_stock']
    return forecast
