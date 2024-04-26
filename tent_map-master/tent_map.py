"""
Usage:\n
tm = new TentMap(0.5)\n
tm.find_distribution(1000)\n
tent_map.plot()
"""
from math import fabs
import numpy as np
import matplotlib.pyplot as plt


class TentMap:
    """Tent map class"""

    def __init__(self, initial_cond, parts=10):
        """
        Tent map constructor.\n
        initial_cond - x_0;\n
        parts - the number of parts on which [0; 1] segment will be divided;
        """
        self.initial_cond = initial_cond
        self.parts = parts
        self.frequency = np.zeros([self.parts])
        self.x_parts = np.linspace(0, 1, self.parts)

    def add_value(self, value):
        """It adds a new element into frequency array"""
        idx = np.searchsorted(self.x_parts, value, side='left')
        if idx > 0 and (idx == len(self.x_parts) or fabs(value - self.x_parts[idx - 1]) <
                        fabs(value - self.x_parts[idx])):
            idx -= 1
        self.frequency[idx] += 1

    def find_distribution(self, alpha=2, iterations=100):
        """
        It iterates a tent map with initial_cond as the initial condition
        """
        if alpha < 1:
            alpha = 1 / alpha
        x_n = self.initial_cond
        self.add_value(x_n)
        for _ in range(1, iterations):
            if x_n >= 0 and x_n < 1 / alpha:
                x_n = alpha * x_n
            elif x_n >= 1 / alpha and x_n <= 1:
                x_n = (alpha / (alpha - 1)) * (1 - x_n)
            self.add_value(x_n)

    def plot(self):
        """It plots histogram"""
        plt.hist(self.x_parts, self.parts, weights=self.frequency)
        plt.show()
