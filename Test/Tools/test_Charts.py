from unittest import TestCase
import Tools.Charts as tools
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class TestCharts(TestCase):

    title = "Test Data"
    xlabel = "X-axis"
    ylabel = "Y-axis"
    values = [{"x": datetime(2000, 1, 1, 0, 0, 0), "y": 0},
              {"x": datetime(2000, 1, 1, 1, 0, 0), "y": 1},
              {"x": datetime(2000, 1, 1, 2, 0, 0), "y": 2},
              {"x": datetime(2000, 1, 1, 3, 0, 0), "y": 3},
              {"x": datetime(2000, 1, 1, 4, 0, 0), "y": 4}
    ]

    def test_Charts_can_instantiate(self):
        try:
            obj = tools.Charts()
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

        self.assertIsInstance(obj, tools.Charts)

    def test_charts_call_plot_single_axis_with_axis_as_None(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values

            tools.Charts().plot_single_axis(None, my_dict)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with axis set to None.")
        finally:
            plt.close(fig)

    def test_charts_call_plot_single_axis_with_my_dict_as_None(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values

            tools.Charts().plot_single_axis(ax1, None)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with dictionary values set to None.")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_values_only(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)

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
            self.fail(f"test_Charts_plot_single_axis_values_only() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_with_title(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values
            my_dict["title"] = self.title

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_single_axis_with_title() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_with_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values
            my_dict["xlabel"] = self.xlabel

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)
            self.assertEqual(self.xlabel, ax2.get_xlabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_single_axis_with_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_with_None_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values
            my_dict["xlabel"] = None

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)
            self.assertEqual("x-axis label not defined", ax2.get_xlabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_single_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_with_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values
            my_dict["ylabel"] = self.ylabel

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)
            self.assertEqual(self.ylabel, ax2.get_ylabel())
            # plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_single_axis_with_y_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_single_axis_with_None_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values
            my_dict["ylabel"] = None

            ax2 = tools.Charts().plot_single_axis(ax1, my_dict)
            self.assertEqual("y-axis label not defined", ax2.get_ylabel())
            plt.show()  # This will actually show the plot
        except Exception as e:
            self.fail(f"test_Charts_plot_single_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)