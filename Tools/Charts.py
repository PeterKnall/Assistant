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

    def plot_axis(self, ax, my_dict):
        """
        Plots a single axis of a figure using the values in the dictionary "dict".  There can be multiple plots
        on a single axis.

        :param ax: Reference to axis to plot
        :param dict: Dictionary containing information to plot.  Key:Value pairs are:
            title:  string title for this set of data
            data:   List of dictionaries. Each dictionary entry contains name:value pairs for names "x" and "y".
        :return: updated axis
        """
        df = pd.DataFrame(my_dict["values"])
        ax.plot(df["x"], df["y"])
        label = ""

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

        if "data_series_1_label" in my_dict:
            if my_dict["data_series_1_label"]:
                ax.get_lines()[0].set_label(my_dict["data_series_1_label"])
            else:
                ax.get_lines()[0].set_label("label not defined")

        return ax