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

    def plot_single_axis(self, ax, my_dict):
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
        if "title" in my_dict:
            ax.set_title(my_dict["title"])
        if "xlabel" in my_dict:
            ax.set_xlabel(my_dict["xlabel"])
        return ax