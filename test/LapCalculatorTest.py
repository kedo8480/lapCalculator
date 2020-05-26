import unittest
from lapCalculator.LapCalculator import *


class TestLapCalculatorMethods(unittest.TestCase):

    def test_ingestData(self):
        result = ingestCSVData("testfile1.csv")

        ingested_data = {"Hamilton": [4.45, 4.22, 4.42], "Knope": [4.33, 4.55, 3.98], "Sabine": [3.99, 5.00, 4.00]}

        self.assertDictEqual(result, ingested_data)

    def test_ingestData_empty(self):
        with self.assertRaises(Exception): ingestCSVData("emptytestfile.csv")

    def test_calculateAvgs(self):
        test_data = {"driver1": [2.2, 2.2, 2.2], "driver2": [2.306, 4.447, 6.891], "driver3": [3, 6, 9]}

        result = calculateAvgs(test_data)

        test_data_avgs = {"driver1": 2.20, "driver2": 4.55, "driver3": 6.00}

        self.assertDictEqual(result, test_data_avgs)

    def test_calculateAvgs_negative(self):
        test_data = {"driver": [3.20, -5.00, 4.34]}

        with self.assertRaises(Exception): calculateAvgs(test_data)

    def test_topN(self):
        average_dictionary = {"driver1": 4.53, "driver2": 4.54, "driver3": 5.99, "driver4": 8.77, "driver5": 3.22,
                              "driver6": 9.93, "driver7": 10.09, "driver8": 2.87}

        result_3 = topN(average_dictionary, 3)
        result_5 = topN(average_dictionary, 5)

        top_list_3 = [["driver8", 2.87], ["driver5", 3.22], ["driver1", 4.53]]

        top_list_5 = [["driver8", 2.87], ["driver5", 3.22], ["driver1", 4.53], ["driver2", 4.54], ["driver3", 5.99]]

        self.assertListEqual(result_3, top_list_3)
        self.assertListEqual(result_5, top_list_5)

    def test_exportCSVData(self):
        top_list = [["smith", 4.44], ["granny", 8.79], ["apple", 3.41]]

        result = exportCSVData(top_list, "testexportfile.csv")
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
