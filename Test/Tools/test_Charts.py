from unittest import TestCase
import Tools.Charts as tools
import pandas as pd
import matplotlib.pyplot as plt


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





