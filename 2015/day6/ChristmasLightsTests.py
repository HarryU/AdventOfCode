import ChristmasLights
import numpy as np
import numpy.testing as nptest
import unittest


class ChristmasLightsTests(unittest.TestCase):
    def setUp(self):
        self.testArrayAllOn = np.ones((1000, 1000))
        self.testArrayAllOff = np.zeros((1000, 1000))

    def test_On0_0through999_999Works(self):
        christmasLights = ChristmasLights.ChristmasLights()
        christmasLights.Change('toggle 0,0 through 999,999')
        nptest.assert_array_equal(self.testArrayAllOn, christmasLights.lights)

    def test_TurnOn0_0Through999_999(self):
        christmasLights = ChristmasLights.ChristmasLights()
        christmasLights.Change('turn on 0,0 through 999,999')
        nptest.assert_array_equal(self.testArrayAllOn, christmasLights.lights)

    def test_TurnOff0_0Through999_999(self):
        christmasLights = ChristmasLights.ChristmasLights()
        christmasLights.Change('turn off 0,0 through 999,999')
        nptest.assert_array_equal(self.testArrayAllOff, christmasLights.lights)