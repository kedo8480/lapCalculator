import unittest
import sys
sys.path.insert(1, "/Users/kdowd954/DEInterviewMaterials/app")
from LapCalculator import *

class TestLapCalculatorMethods(unittest.TestCase):

    def test_ingestData(self):
        result = ingestCSVData("testfile1.csv")

        ingested_data = {}
        ingested_data["Hamilton"] = [4.45,4.22,4.42]
        ingested_data["Knope"] = [4.33,4.55,3.98]
        ingested_data["Sabine"] = [3.99,5.00,4.00]
        
        self.assertDictEqual(result, ingested_data)

    def test_ingestData_empty(self):
        with self.assertRaises(Exception): ingestCSVData("emptytestfile.csv")

    def test_calculateAvgs(self):
        test_data = {}
        test_data["driver1"] = [2.2, 2.2, 2.2]
        test_data["driver2"] = [2.306, 4.447, 6.891]
        test_data["driver3"] = [3, 6, 9]

        result = calculateAvgs(test_data)

        test_data_avgs = {}
        test_data_avgs["driver1"] = 2.20
        test_data_avgs["driver2"] = 4.55
        test_data_avgs["driver3"] = 6.00
        
        self.assertDictEqual(result, test_data_avgs)

    def test_calculateAvgs_negative(self):
        test_data = {}
        test_data["driver"] = [3.20,-5.00,4.34]

        with self.assertRaises(Exception): calculateAvgs(test_data)

    def test_topN(self):
        average_dictionary = {}
        average_dictionary["driver1"] = 4.53
        average_dictionary["driver2"] = 4.54
        average_dictionary["driver3"] = 5.99
        average_dictionary["driver4"] = 8.77
        average_dictionary["driver5"] = 3.22
        average_dictionary["driver6"] = 9.93
        average_dictionary["driver7"] = 10.09
        average_dictionary["driver8"] = 2.87

        result_3 = topN(average_dictionary, 3)
        result_5 = topN(average_dictionary, 5)

        top_list_3 = []
        top_list_3.append(["driver8", 2.87])
        top_list_3.append(["driver5", 3.22])
        top_list_3.append(["driver1", 4.53])

        top_list_5 = []
        top_list_5.append(["driver8", 2.87])
        top_list_5.append(["driver5", 3.22])
        top_list_5.append(["driver1", 4.53])
        top_list_5.append(["driver2", 4.54])
        top_list_5.append(["driver3", 5.99])

        self.assertListEqual(result_3, top_list_3)
        self.assertListEqual(result_5, top_list_5)

    def test_exportCSVData(self):
        top_list = []
        top_list.append(["smith", 4.44])
        top_list.append(["granny", 8.79])
        top_list.append(["apple", 3.41])
        
        result = exportCSVData(top_list, "testexportfile.csv")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()