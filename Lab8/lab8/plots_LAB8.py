import matplotlib.pyplot as plt

#дані і методи в одному класі
class CombinedPlot:
    def __init__(self, ax, data):
        self.ax = ax
        self.data = data

    def plot(self):
        game_counts = self.data['radiant_win'].value_counts().sort_index()
        avg_mmr_by_result = self.data.groupby('radiant_win')['avg_mmr'].mean().sort_index()

        print("\nКількість ігор (виграш/програш):")
        print(game_counts)
        print("\nСередній MMR за результатом гри:")
        print(avg_mmr_by_result)

        ax2 = self.ax.twinx()

        if not game_counts.empty:
            self.ax.bar(game_counts.index, game_counts.values, color='blue', alpha=0.5, label='Кількість ігор')
            self.ax.set_ylim(0, game_counts.values.max() * 1.1)
            self.ax.set_xticks(game_counts.index)
            self.ax.set_xticklabels(['Програш', 'Виграш'])

        if not avg_mmr_by_result.empty:
            ax2.plot(avg_mmr_by_result.index, avg_mmr_by_result.values, color='red', marker='o', label='Середній MMR')
            ax2.set_ylim(0, avg_mmr_by_result.values.max() * 1.1)

        self.ax.set_xlabel('Результат гри')
        self.ax.set_ylabel('Кількість ігор', color='blue')
        ax2.set_ylabel('Середній MMR', color='red')
        self.ax.legend(loc='upper left')
        ax2.legend(loc='upper right')

class HistogramPlot:
    def __init__(self, ax, data, column, title, color):
        self.ax = ax
        self.data = data
        self.column = column
        self.title = title
        self.color = color

    def plot(self):
        self.ax.hist(self.data[self.column], bins=20, color=self.color, edgecolor='black')
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.column)
        self.ax.set_ylabel('Частота')
