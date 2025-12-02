from unittest import TestCase
import Tools.Charts as tools
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class TestCharts(TestCase):

    def test_Charts_can_instantiate(self):
        try:
            obj = tools.Charts()
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

        self.assertIsInstance(obj, tools.Charts)

    def test_charts_call_plot_single_axis(self):
        try:
            obj = tools.Charts()
            obj.plot_single_axis(None, None)
        except Exception as e:
            self.fail(f"Failed to call plot_single_axis(): {e}")

    def test_Charts_plot_single_axis(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["title"] = "test_Charts_plot_single_axis"
            values = [{"x" : datetime(2000, 1, 1, 0, 0, 0), "y": 0},
                         {"x" : datetime(2000, 1, 1, 1, 0, 0), "y": 1},
                         {"x" : datetime(2000, 1, 1, 2, 0, 0), "y": 2},
                         {"x" : datetime(2000, 1, 1, 3, 0, 0), "y": 3},
                         {"x" : datetime(2000, 1, 1, 4, 0, 0), "y": 4}
            ]
            my_dict["values"] = values

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
            self.fail(f"Call to generate_trend_chart() failed: {e}")



