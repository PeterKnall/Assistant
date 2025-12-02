from unittest import TestCase
import Tools.Charts as tools
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


class TestCharts(TestCase):

    show_plot = True
    x_label = "X-axis"
    y_label = "Y-axis"
    data_series_1_label = "Data Series 1"
    data_series_2_label = "Data Series 2"
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

        self.assertIsInstance(obj, tools.Charts, "Object is not an instance of Tools.Charts.Charts()")

    def test_Charts_call_plot_axis_with_axis_as_None_returns_exception(self):
        try:
            my_dict = dict()
            my_dict["values"] = self.values_1

            tools.Charts().plot_axis(None, my_dict)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with axis set to None.")

    def test_Charts_call_plot_axis_with_my_dict_as_None_returns_exception(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

            tools.Charts().plot_axis(ax, None)
        except Exception as e:
            pass
        else:
            self.assertFalse(f"Expected exception when calling with dictionary values set to None.")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_empty_dataframe_returns_exception(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()

            tools.Charts().plot_axis(ax, my_dict)
        except Exception as e:
            pass
        else:
            self.fail(f"test_Charts_plot_axis_with_empty_dataframe() failed")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_values_only(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_values_only")
            my_dict = dict()
            my_dict["values"] = self.values_1

            tools.Charts().plot_axis(ax, my_dict)

            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(1, len(ax.get_lines()), "There is not 1 line in the axis")
            self.assertEqual(5, len(ax.get_lines()[0].get_xdata()), "There are not 5 data points on the x-axis")
            self.assertEqual(5, len(ax.get_lines()[0].get_ydata()), "There are not 5 data points on the y-axis")

            x_values = ax.get_lines()[0].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0],
                             "test_Charts_plot_axis_values_only: x-axis[0] failed")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1],
                             "test_Charts_plot_axis_values_only: x-axis[1] failed")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2],
                             "test_Charts_plot_axis_values_only: x-axis[2] failed")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3],
                             "test_Charts_plot_axis_values_only: x-axis[3] failed")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4],
                             "test_Charts_plot_axis_values_only: x-axis[4] failed")

            y_values = ax.get_lines()[0].get_ydata()
            self.assertEqual(0, y_values[0],
                             "test_Charts_plot_axis_values_only: y-axis[0] failed")
            self.assertEqual(1, y_values[1],
                             "test_Charts_plot_axis_values_only: y-axis[1] failed")
            self.assertEqual(2, y_values[2],
                             "test_Charts_plot_axis_values_only: y-axis[2] failed")
            self.assertEqual(3, y_values[3],
                             "test_Charts_plot_axis_values_only: y-axis[3] failed")
            self.assertEqual(4, y_values[4],
                             "test_Charts_plot_axis_values_only: y-axis[4] failed")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_values_only() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_two_axis_values(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_two_axis_values")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict2 = dict()
            my_dict2["values"] = self.values_2

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertIsInstance(ax, plt.Axes)
            self.assertEqual(2, len(ax.get_lines()),
                             "test_Charts_plot_two_axis_values: There are not 2 lines in the axis")
            self.assertEqual(5, len(ax.get_lines()[0].get_xdata()),
                             "test_Charts_plot_two_axis_values: There are not 5 data points on the x-axis in line 1")
            self.assertEqual(5, len(ax.get_lines()[0].get_ydata()),
                             "test_Charts_plot_two_axis_values: There are not 5 data points on the y-axis in line 1")

            x_values = ax.get_lines()[0].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0],
                             "test_Charts_plot_two_axis_values: x-axis[0] failed in line 1")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1],
                             "test_Charts_plot_two_axis_values: x-axis[1] failed in line 1")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2],
                             "test_Charts_plot_two_axis_values: x-axis[2] failed in line 1")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3],
                             "test_Charts_plot_two_axis_values: x-axis[3] failed in line 1")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4],
                             "test_Charts_plot_two_axis_values: x-axis[4] failed in line 1")

            y_values = ax.get_lines()[0].get_ydata()
            self.assertEqual(0, y_values[0],
                             "test_Charts_plot_two_axis_values: y-axis[0] failed in line 1")
            self.assertEqual(1, y_values[1],
                             "test_Charts_plot_two_axis_values: y-axis[1] failed in line 1")
            self.assertEqual(2, y_values[2],
                             "test_Charts_plot_two_axis_values: y-axis[2] failed in line 1")
            self.assertEqual(3, y_values[3],
                             "test_Charts_plot_two_axis_values: y-axis[3] failed in line 1")
            self.assertEqual(4, y_values[4],
                             "test_Charts_plot_two_axis_values: y-axis[4] failed in line 1")

            self.assertEqual(5, len(ax.get_lines()[1].get_xdata()),
                             "test_Charts_plot_two_axis_values: There are not 5 data points on the x-axis in line 2")
            self.assertEqual(5, len(ax.get_lines()[1].get_ydata()),
                             "test_Charts_plot_two_axis_values: There are not 5 data points on the y-axis in line 2")

            x_values = ax.get_lines()[1].get_xdata()
            self.assertEqual(np.datetime64("2000-01-01T00:00:00.000000000"), x_values[0],
                             "test_Charts_plot_two_axis_values: x-axis[0] failed in line 2")
            self.assertEqual(np.datetime64("2000-01-01T01:00:00.000000000"), x_values[1],
                             "test_Charts_plot_two_axis_values: x-axis[1] failed in line 2")
            self.assertEqual(np.datetime64("2000-01-01T02:00:00.000000000"), x_values[2],
                             "test_Charts_plot_two_axis_values: x-axis[2] failed in line 2")
            self.assertEqual(np.datetime64("2000-01-01T03:00:00.000000000"), x_values[3],
                             "test_Charts_plot_two_axis_values: x-axis[3] failed in line 2")
            self.assertEqual(np.datetime64("2000-01-01T04:00:00.000000000"), x_values[4],
                             "test_Charts_plot_two_axis_values: x-axis[4] failed in line 2")

            y_values = ax.get_lines()[1].get_ydata()
            self.assertEqual(4, y_values[0],
                             "test_Charts_plot_two_axis_values: y-axis[4] failed in line 2")
            self.assertEqual(3, y_values[1],
                             "test_Charts_plot_two_axis_values: y-axis[3] failed in line 2")
            self.assertEqual(2, y_values[2],
                             "test_Charts_plot_two_axis_values: y-axis[2] failed in line 2")
            self.assertEqual(1, y_values[3],
                             "test_Charts_plot_two_axis_values: y-axis[1] failed in line 2")
            self.assertEqual(0, y_values[4],
                             "test_Charts_plot_two_axis_values: y-axis[0] failed in line 2")

            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_two_axis_values() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_title(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["title"] = "test_Charts_plot_axis_with_title"

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual(my_dict["title"], ax.get_title(),
                             "test_Charts_plot_axis_with_title: test_Charts_plot_axis_with_title: Title did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_title() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_title(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["title"] = None

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual("title not defined", ax.get_title(),
                             "test_Charts_plot_axis_with_None_title: None title assert failed")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_title() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_x_axis_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["x_label"] = self.x_label

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual(self.x_label, ax.get_xlabel(),
                             "test_Charts_plot_axis_with_x_axis_label: x-axis labels did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_x_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_None_x_axis_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["x_label"] = None

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual("x-axis label not defined", ax.get_xlabel(),
                             "test_Charts_plot_axis_with_None_x_axis_label: None x-axis label assert failed")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_y_axis_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["y_label"] = self.y_label

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual(self.y_label, ax.get_ylabel(),
                             "test_Charts_plot_axis_with_y_axis_label: y-axis labels did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_y_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_y_axis_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_None_y_axis_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["y_label"] = None

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual("y-axis label not defined", ax.get_ylabel(),
                             "test_Charts_plot_axis_with_None_y_axis_label: y-axis label assert failed")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_x_axis_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_data_series_1_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_data_series_1_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["data_series_label"] = self.data_series_1_label

            tools.Charts().plot_axis(ax, my_dict)

            self.assertEqual(my_dict["data_series_label"], ax.get_lines()[0].get_label(),
                             "test_Charts_plot_axis_with_data_series_1_label: series 1 labels did not match")
            if self.show_plot:
                plt.legend()
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_data_series_1_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_data_series_2_label(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_data_series_2_label")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["data_series_label"] = self.data_series_1_label
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["data_series_label"] = self.data_series_2_label

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual(my_dict1["data_series_label"], ax.get_lines()[0].get_label(),
                             "test_Charts_plot_axis_with_data_series_2_label: series 1 labels did not match")
            self.assertEqual(my_dict2["data_series_label"], ax.get_lines()[1].get_label(),
                             "test_Charts_plot_axis_with_data_series_2_label: series 2 labels did not match")

            if self.show_plot:
                plt.legend()
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_data_series_1_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_data_series_1_label(self):
        try:
            fig = plt.figure(figsize=(10, 5))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_None_data_series_1_label")
            my_dict = dict()
            my_dict["values"] = self.values_1
            my_dict["data_series_label"] = None

            tools.Charts().plot_axis(ax, my_dict)
            self.assertEqual("label not defined", ax.get_lines()[0].get_label(),
                             "test_Charts_plot_axis_with_None_data_series_1_label: series 1 label assert fail")
            if self.show_plot:
                plt.legend()
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_data_series_1_label() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_text_color(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_text_color")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["color"] = "red"
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["color"] = "green"

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual("red", ax.get_lines()[0].get_color(),
                             "test_Charts_plot_axis_with_text_color: line 1 color did not match")
            self.assertEqual("green", ax.get_lines()[1].get_color(),
                             "test_Charts_plot_axis_with_text_color: line 2 color did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_text_color() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_hex_color(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_hex_color")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["color"] = "#FF0000"
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["color"] = "#00FF00"

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual("#FF0000", ax.get_lines()[0].get_color(),
                             "test_Charts_plot_axis_with_hex_color: line 1 color did not match")
            self.assertEqual("#00FF00", ax.get_lines()[1].get_color(),
                             "test_Charts_plot_axis_with_hex_color: line 2 color did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_hex_color() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_rgb_color(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_rgb_color")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["color"] = (1, 0, 0)
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["color"] = (0, 1, 0)

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual((1, 0, 0), ax.get_lines()[0].get_color(),
                             "test_Charts_plot_axis_with_rgb_color: line 1 color did not match")
            self.assertEqual((0, 1, 0), ax.get_lines()[1].get_color(),
                             "test_Charts_plot_axis_with_rgb_color: line 2 color did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_rgb_color() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_color(self):
        try:
            colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]      # Uses the matplotlib color cycle

            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_None_color")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["color"] = None
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["color"] = None

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual(colors[0], ax.get_lines()[0].get_color(),
                             "test_Charts_plot_axis_with_None_color: line 1 color did not match color cycle")
            self.assertEqual(colors[1], ax.get_lines()[1].get_color(),
                             "test_Charts_plot_axis_with_None_color: line 2 color did not match color cycle")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_None_color() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_invalid_color(self):
        try:
            colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]      # Uses the matplotlib color cycle

            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_invalid_color")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["color"] = "Not a valid color"
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["color"] = "Also not a valid color"

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual(colors[0], ax.get_lines()[0].get_color(),
                             "test_Charts_plot_axis_with_invalid_color: line 1 color did not match color cycle")
            self.assertEqual(colors[1], ax.get_lines()[1].get_color(),
                             "test_Charts_plot_axis_with_invalid_color: line 2 color did not match color cycle")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_invalid_color() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_marker(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_marker")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["marker"] = "o"
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["marker"] = "x"

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual("o", ax.get_lines()[0].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 1 did not match")
            self.assertEqual("x", ax.get_lines()[1].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 2 did not match")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_marker() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_None_marker(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_None_marker")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["marker"] = None
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["marker"] = None

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual("None", ax.get_lines()[0].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 1 is not None")
            self.assertEqual("None", ax.get_lines()[1].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 2 is not None")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_marker() failed: {e}")
        finally:
            plt.close(fig)

    def test_Charts_plot_axis_with_invalid_marker(self):
        try:
            fig = plt.figure(figsize=(15, 9))
            ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
            ax.set_title("test_Charts_plot_axis_with_invalid_marker")
            my_dict1 = dict()
            my_dict1["values"] = self.values_1
            my_dict1["marker"] = "/"
            my_dict2 = dict()
            my_dict2["values"] = self.values_2
            my_dict2["marker"] = "M"

            tools.Charts().plot_axis(ax, my_dict1)
            tools.Charts().plot_axis(ax, my_dict2)

            self.assertEqual("None", ax.get_lines()[0].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 1 is not None")
            self.assertEqual("None", ax.get_lines()[1].get_marker(),
                             "test_Charts_plot_axis_with_marker: marker 2 is not None")
            if self.show_plot:
                plt.show()
        except Exception as e:
            self.fail(f"test_Charts_plot_axis_with_marker() failed: {e}")
        finally:
            plt.close(fig)