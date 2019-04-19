import matplotlib.pyplot as plt
import pandas as pd


"""
Wind Class, reads csv file. Creates an object with all data
"""


class Wind:

    def __init__(self):
        self.df = pd.read_csv('/home/ibalab/PycharmProjects/module1/files/windData20190416.csv')

    def get_wind_array(self):
        """

        :return:
        :rtype:
        """
        plt.plot(self.df.Speed)
        plt.show()
        return self.df.Speed
