from unittest import TestCase

import Tools.Charts
import Tools.Charts as tools


class TestCharts(TestCase):

    def test_Charts_can_instantiate(self):
        try:
            obj = tools.Charts()
        except Exception as e:
            self.fail(f"Instantiation failed: {e}")

        self.assertIsInstance(obj, tools.Charts)
