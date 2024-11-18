import pandas as pd

def load_and_preprocess(csv_file):
    data = pd.read_csv(csv_file)
    print("Унікальні значення перед мапінгом:", data['radiant_win'].unique())

    data['radiant_win'] = data['radiant_win'].map({True: 1, False: 0})
    print("Унікальні значення після мапінгу:", data['radiant_win'].unique())

    data.dropna(subset=['avg_mmr', 'duration'], inplace=True)

    print("\nОпис середнього MMR:")
    print(data['avg_mmr'].describe())
    print("\nОпис тривалості ігор:")
    print(data['duration'].describe())
    print("\nКількість пропущених значень у 'avg_mmr':", data['avg_mmr'].isnull().sum())
    print("Кількість пропущених значень у 'duration':", data['duration'].isnull().sum())
    print("\nРозмір датафрейму після видалення пропусків:", data.shape)
    return data

