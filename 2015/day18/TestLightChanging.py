import numpy as np
import numpy.testing as nptest
import unittest


class TestLightChanging(unittest.TestCase):
    def setUp(self):
        testInitialState = np.array([[False, True, False, True, False, True],
                                     [False, False, False, True, True, False],
                                     [True, False, False, False, False, True],
                                     [False, False, True, False, False, False],
                                     [True, False, True, False, False, True],
                                     [True, True, True, False, False, False]])
        self.lights = LightChanging(testInitialState)

    def test_AfterStepOne(self):
        testStepOneState = np.array([[False, False, True, True, False, False],
                                     [False, False, True, True, False, True],
                                     [False, False, False, True, True, False],
                                     [False, False, False, False, False, False],
                                     [True, False, False, False, False, False],
                                     [True, False, True, True, False, False]])
        self.lights.TakeSteps(1)
        nptest.assert_array_equal(testStepOneState, self.lights.currentConfiguration)


class LightChanging:
    def __init__(self, initialState):
        self.currentConfiguration = initialState

    def TakeSteps(self, n):
        for _ in range(n):
            for i in range(self.currentConfiguration.shape[0]):
                for j in range(self.currentConfiguration.shape[1]):
                    pass