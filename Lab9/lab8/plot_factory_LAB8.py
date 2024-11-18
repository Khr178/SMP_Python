from .plots_LAB8 import CombinedPlot, HistogramPlot

#можливість викликати один метод plot для різних типів графіків
#патерн, який допомагає створювати об’єкти певного типу, не вказуючи конкретний клас, а лише тип.
class PlotFactory:
    @staticmethod
    def create_plot(plot_type, ax, data, *args):
        if plot_type == 'combined':
            return CombinedPlot(ax, data)
        elif plot_type == 'histogram':
            return HistogramPlot(ax, data, *args)
        else:
            raise ValueError(f"Unknown plot type: {plot_type}")
