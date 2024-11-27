

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
'''
for t in truth:
	print(t)
	print(type(t))
	print("--------------------")'''

	
