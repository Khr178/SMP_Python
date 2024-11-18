from BLL.plot_factory_LAB8 import PlotFactory

def plot_combined_chart(ax, data):
    combined_plot = PlotFactory.create_plot('combined', ax, data)
    combined_plot.plot()

def plot_histogram(ax, data, column, title, color):
    histogram_plot = PlotFactory.create_plot('histogram', ax, data, column, title, color)
    histogram_plot.plot()

