import matplotlib.pyplot as plt
from DAL.data_loader_LAB8 import load_and_preprocess
from BLL.data_explorer_LAB8 import explore_data
from UI.visualizations_LAB8 import plot_combined_chart, plot_histogram

def run():
    data = load_and_preprocess('Data/games_cleaned.csv')

    explore_data(data)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    plot_combined_chart(axes[0], data)
    plot_histogram(axes[1], data, 'avg_mmr', 'Гістограма середнього MMR', 'skyblue')
    plot_histogram(axes[2], data, 'duration', 'Гістограма тривалості ігор', 'salmon')

    fig.suptitle('Результати ігор та статистика')
    plt.tight_layout()
    plt.subplots_adjust(top=0.88)
    plt.savefig('Data/game_results_and_statistics.png')
    plt.show()

if __name__ == "__main__":
        run()