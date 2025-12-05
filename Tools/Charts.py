import pandas as pd
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

class Charts:
    """
    Charting tools to handle data returned from various Building Automation System APIs.  Notes on creating charts:
    1) There are one or more child charts (axes) that are a part of a parent chart (figure).
    2) Each chart requires a title.
    3) Each chart may have different units for x and y values
    """
    def __init__(self):
        pass

    def build_figure(self, axes_list):
        """
        Build a figure from design list (DL) of data_dict_lists.  DLs are templates for the data an axis should contain
        based on the information it intends to convey.

        For example, if the DL is for the performance of Room Temperature versus Setpoint, then processing the DL
        using the Building Automation System's (BAS) API will return data_dict_lists containing the Room Temperature,
        Current Heating Setpoint, and Current Cooling Setpoint

        :param axes_list:
        :return: figure: Matplotlib pyplot figure containing all the axes
        """
        if axes_list is None:
            message = "Axis List is None in Charts.build_figure()"
            logger.error(f"Exception:  {message}")
            raise Exception(message)

        figure = plt.figure()
        return figure

    def build_axis(self, ax, data_dict_list):
        """
        Plot one or more collections of data on a single axis.
        :param ax: The axis to attach the data to
        :param data_dict_list: A list of dictionaries containing the data to apply to the axis
        :return: axis with data plotted
        """
        logger.info("Entering Charts.build_axis()")
        for data_dict in data_dict_list:
            logger.info(f"Processing {data_dict}")
            self.plot_data(ax, data_dict)

        logger.info("Leaving Charts.build_axis()")
        return ax

    def plot_data(self, ax, data_dict):
        """
        Plots a single axis of a figure using the values in the dictionary "data_dict".  There can be multiple plots
        on a single axis.

        :param ax: Reference to axis to plot
        :param data_dict: Dictionary containing information to plot.  Key:Value pairs are:
            title:  string title for this set of data
            x_label: label for the x-axis
            y_label: label for the y-axis
            data_series_label: label for the data series in the legend
            color: string name, string hexadecimal value, or RGB tuple for line color
                        if an invalid color is selected, the matplotlib pyplot color cycle is used
            marker: string assignment for a marker for the data points in ['o', '.', 's', '^', 'v', 'x', '+', '*', 'D']
                        if an invalid marker is used, none will be shown
            data:   List of dictionaries. Each dictionary entry contains one data sample for
                        name:value pairs "x" and "y".
        :return: updated axis
        """
        logger.info("Entering Charts.plot_data()")
        df = pd.DataFrame(data_dict["values"])
        ax.plot(df["x"], df["y"])

        if "title" in data_dict:
            if data_dict["title"]:
                ax.set_title(data_dict["title"])
            else:
                ax.set_title("title not defined")

        if "x_label" in data_dict:
            if data_dict["x_label"]:
                ax.set_xlabel(data_dict["x_label"])
            else:
                ax.set_xlabel("x-axis label not defined")

        if "y_label" in data_dict:
            if data_dict["y_label"]:
                ax.set_ylabel(data_dict["y_label"])
            else:
                ax.set_ylabel("y-axis label not defined")

        if "data_series_label" in data_dict:
            index = len(ax.get_lines()) - 1
            if data_dict["data_series_label"]:
                ax.get_lines()[index].set_label(data_dict["data_series_label"])
            else:
                logger.error(f"Label assigned but not defined in: {data_dict}")
                ax.get_lines()[index].set_label("label not defined")

        if "color" in data_dict:
            index = len(ax.get_lines()) - 1
            if data_dict["color"]:
                try:
                    ax.get_lines()[index].set_color(data_dict["color"])
                except Exception as e:
                    logger.error(f"Color assigned but not defined in: {data_dict}")
            else:
                pass   # if None is passed, do nothing

        if "marker" in data_dict:
            index = len(ax.get_lines()) - 1
            if data_dict["marker"]:
                try:
                    ax.get_lines()[index].set_marker(data_dict["marker"])
                except Exception as e:
                    logger.error(f"Marker assigned but not defined in: {data_dict}")
            else:
                pass        # do nothing

        logger.info("Leaving Charts.plot_data()")
        return ax