from unittest import TestCase

import pandas as pd

import Tools.Charts as tools
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class TestCharts(TestCase):

    title = "Test Data"
    x_label = "X-axis"
    y_label = "Y-axis"
    data_series_1_label = "Data Series 1"
    values_1 = [{"x": datetime(2000, 1, 1, 0, 0, 0), "y": 0},
                {"x": datetime(2000, 1, 1, 1, 0, 0), "y": 1},
                {"x": datetime(2000, 1, 1, 2, 0, 0), "y": 2},
                {"x": datetime(2000, 1, 1, 3, 0, 0), "y": 3},
                {"x": datetime(2000, 1, 1, 4, 0, 0), "y": 4}
                ]
    values_2 = [{"x": datetime(2000, 1, 1, 0, 0, 0), "y": 4},
                {"x": datetime(2000, 1, 1, 1, 0, 0), "y": 3},
                {"x": datetime(2000, 1, 1, 2, 0, 0), "y": 2},
                {"x": datetime(2000, 1, 1, 3, 0, 0), "y": 1},
                {"x": datetime(2000, 1, 1, 4, 0, 0), "y": 0}
                ]
    def test_Charts_can_instantiate(self):
        try:
            obj = tools.Charts()
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

        self.assertIsInstance(obj, tools.Charts)

    def test_charts_call_plot_axis_with_axis_as_None_returns_exception(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1

            tools.Charts().plot_axis(None, my_dict)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with axis set to None.")
        finally:
            plt.close(fig)

    def test_charts_call_plot_axis_with_my_dict_as_None_returns_exception(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1

            tools.Charts().plot_axis(ax1, None)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with dictionary values set to None.")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_empty_dataframe_returns_exception(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
        except Exception as e:
            pass
        else:
            self.fail(f"test_Charts_plot_axis_with_empty_dataframe() failed")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_values_only(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1

            ax2 = tools.Charts().plot_axis(ax1, my_dict)

            self.assertIsInstance(ax2, plt.Axes)
            self.assertEqual(1, len(ax2.get_lines()), "There is not 1 line in the axis")
            self.assertEqual(5, len(ax2.get_lines()[0].get_xdata()), "There are not 5 data points on the x-axis")
            self.assertEqual(5, len(ax2.get_lines()[0].get_ydata()), "There are not 5 data points on the y-axis")

            x_values = ax2.get_lines()[0].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0], "x-axis[0] failed")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1], "x-axis[1] failed")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2], "x-axis[2] failed")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3], "x-axis[3] failed")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4], "x-axis[4] failed")

            y_values = ax2.get_lines()[0].get_ydata()
            self.assertEqual(0, y_values[0], "y-axis[0] failed")
            self.assertEqual(1, y_values[1], "y-axis[1] failed")
            self.assertEqual(2, y_values[2], "y-axis[2] failed")
            self.assertEqual(3, y_values[3], "y-axis[3] failed")
            self.assertEqual(4, y_values[4], "y-axis[4] failed")
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_values_only() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_two_axis_values(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict2 = dict()
            my_dict2["values"] = self.values_2

            ax2 = tools.Charts().plot_axis(ax1, my_dict1)
            ax3 = tools.Charts().plot_axis(ax1, my_dict2)

            self.assertIsInstance(ax2, plt.Axes)
            self.assertEqual(2, len(ax2.get_lines()), "There are not 2 lines in the axis")
            self.assertEqual(5, len(ax2.get_lines()[0].get_xdata()),
                             "There are not 5 data points on the x-axis")
            self.assertEqual(5, len(ax2.get_lines()[0].get_ydata()),
                             "There are not 5 data points on the y-axis")

            x_values = ax2.get_lines()[0].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0], "x-axis[0] failed")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1], "x-axis[1] failed")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2], "x-axis[2] failed")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3], "x-axis[3] failed")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4], "x-axis[4] failed")

            y_values = ax2.get_lines()[0].get_ydata()
            self.assertEqual(0, y_values[0], "y-axis[0] failed")
            self.assertEqual(1, y_values[1], "y-axis[1] failed")
            self.assertEqual(2, y_values[2], "y-axis[2] failed")
            self.assertEqual(3, y_values[3], "y-axis[3] failed")
            self.assertEqual(4, y_values[4], "y-axis[4] failed")

            self.assertEqual(5, len(ax2.get_lines()[0].get_xdata()),
                             "There are not 5 data points on the x-axis")
            self.assertEqual(5, len(ax2.get_lines()[0].get_ydata()),
                             "There are not 5 data points on the y-axis")

            x_values = ax2.get_lines()[1].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0], "x-axis[0] failed")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1], "x-axis[1] failed")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2], "x-axis[2] failed")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3], "x-axis[3] failed")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4], "x-axis[4] failed")

            y_values = ax2.get_lines()[1].get_ydata()
            self.assertEqual(4, y_values[0], "y-axis[4] failed")
            self.assertEqual(3, y_values[1], "y-axis[3] failed")
            self.assertEqual(2, y_values[2], "y-axis[2] failed")
            self.assertEqual(1, y_values[3], "y-axis[1] failed")
            self.assertEqual(0, y_values[4], "y-axis[0] failed")

            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_values_only() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_title(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["title"] = self.title

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual(my_dict["title"], ax2.get_title())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_title() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_title(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["title"] = None

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual("title not defined", ax2.get_title())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_title() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["x_label"] = self.x_label

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual(self.x_label, ax2.get_xlabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["x_label"] = None

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual("x-axis label not defined", ax2.get_xlabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["y_label"] = self.y_label

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual(self.y_label, ax2.get_ylabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_y_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["y_label"] = None

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual("y-axis label not defined", ax2.get_ylabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_data_series_1_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["data_series_1_label"] = self.data_series_1_label

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual(my_dict["data_series_1_label"], ax2.get_lines()[0].get_label())
            # plt.legend()
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_data_series_1_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_data_series_1_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["data_series_1_label"] = None

            ax2 = tools.Charts().plot_axis(ax1, my_dict)
            self.assertEqual("label not defined", ax2.get_lines()[0].get_label())
            # plt.legend()
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_data_series_1_label() failed: {e}")
        finally:
            pass
            plt.close(fig)