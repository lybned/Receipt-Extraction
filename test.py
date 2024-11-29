
'''
from datasets import load_dataset
from PIL import Image, ImageEnhance
import json
dataset = load_dataset("naver-clova-ix/cord-v1")

#print(dataset['train'][:3])
train_data = dataset['train'][:30]
images = train_data['image']
truth = train_data['ground_truth']
truth = list(map(lambda x: json.loads(x), truth))
print(len(images), len(truth))

for t in truth:
	print(t)
	print(type(t))
	print("--------------------")'''
	
	

import unittest

# List of test directories
test_directories = [
    #"./src/Data",  # Path to the first folder containing test files
    "./src/MLFlow"  # Path to the second folder containing test files
]

# Discover all tests in the "tests" directory
test_loader = unittest.TestLoader()
test_suites = test_loader.discover(start_dir=test_directories[0], pattern="test.py")#[test_loader.discover(start_dir=folder, pattern="test.py") for folder in test_directories]
print(test_suites)
# Combine all suites
combined_suite = unittest.TestSuite(test_suites)

# Run the combined suite
test_runner = unittest.TextTestRunner()
test_runner.run(test_suites)
	
