def explore_data(data):
    for column in data.columns:
        if data[column].dtype.kind in 'biufc':
            min_value = data[column].min()
            max_value = data[column].max()
            print(f"{column}: Мінімальне значення - {min_value}, Максимальне значення - {max_value}")

