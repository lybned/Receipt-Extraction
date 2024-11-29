import unittest
from DataUtil import *
import random

class Test_Class(unittest.TestCase):
	def test_dataset(self):
		data = DataUtil()
		train = data.get_train_data()
		
		ran_length = random.randrange(30, 81)
		image_list = train_data[:ran_length]["image"]
		truth_list = train_data[:ran_length]["ground_truth"]
		truth_list = list(map(lambda x: json.loads(x), truth_list))
		
		self.assertEqual(len(image_list), ran_length, 'Image list has the wrong length.')
		self.assertEqual(len(truth_list), ran_length, 'Truth list has the wrong length.')
	
if __name__ == "__main__":
    unittest.main()