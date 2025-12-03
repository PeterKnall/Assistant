import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Charts:
    """
    Charting tools to handle data returned from various Building Automation System APIs.  Notes on creating charts:
    1) There are one or more child charts (axes) that are a part of a parent chart (figure).
    2) Each chart requires a title.
    3) Each chart may have different units for x and y values
    """
    def __init__(self):
        pass

    def build_axis(self, ax, axis_dict_list):
        """
        Plot one or more collections of data on a single axis.
        :param ax: The axis to attach the data to
        :param axis_dict_list: A list of dictionaries containing the data to apply to the axis
        :return: axis with data plotted
        """
        pass

    def plot_axis(self, ax, my_dict):
        """
        Plots a single axis of a figure using the values in the dictionary "dict".  There can be multiple plots
        on a single axis.

        :param ax: Reference to axis to plot
        :param dict: Dictionary containing information to plot.  Key:Value pairs are:
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
        df = pd.DataFrame(my_dict["values"])
        ax.plot(df["x"], df["y"])

        if "title" in my_dict:
            if my_dict["title"]:
                ax.set_title(my_dict["title"])
            else:
                ax.set_title("title not defined")

        if "x_label" in my_dict:
            if my_dict["x_label"]:
                ax.set_xlabel(my_dict["x_label"])
            else:
                ax.set_xlabel("x-axis label not defined")

        if "y_label" in my_dict:
            if my_dict["y_label"]:
                ax.set_ylabel(my_dict["y_label"])
            else:
                ax.set_ylabel("y-axis label not defined")

        if "data_series_label" in my_dict:
            index = len(ax.get_lines()) - 1
            if my_dict["data_series_label"]:
                ax.get_lines()[index].set_label(my_dict["data_series_label"])
            else:
                ax.get_lines()[index].set_label("label not defined")

        if "color" in my_dict:
            index = len(ax.get_lines()) - 1
            if my_dict["color"]:
                try:
                    ax.get_lines()[index].set_color(my_dict["color"])
                except Exception as e:
                    pass    # defer to Matplotlib pyplot's color cycle
            else:
                pass   # if None is passed, do nothing

        if "marker" in my_dict:
            index = len(ax.get_lines()) - 1
            if my_dict["marker"]:
                try:
                    ax.get_lines()[index].set_marker(my_dict["marker"])
                except Exception as e:
                    pass    # do nothing
            else:
                pass        # do nothing

        return ax