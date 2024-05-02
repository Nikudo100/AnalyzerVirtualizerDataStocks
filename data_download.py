import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def calculate_and_display_average_price(data):
    average_price = data['Close'].mean()
    print(f"Средняя цена закрытия за период: {average_price:.2f}")


def notify_if_strong_fluctuations(data, threshold):
    # Извлечение столбца с ценами закрытия
    closing_prices = data['Close']

    # Рассчет максимального и минимального значения цен
    max_price = closing_prices.max()
    min_price = closing_prices.min()

    # Рассчет процента колебаний
    fluctuation = (max_price - min_price) / min_price * 100

    # Проверяем, превышает ли колебание пороговое значение
    if fluctuation > threshold:
        print(f"Цена акций колебалась более чем на {threshold}% за период.")
    else:
        print("Колебания цены акций не превысили заданный порог.")


def export_data_to_csv(data, filename):
    data.to_csv(filename)
    print(f"Данные сохранены в {filename}")