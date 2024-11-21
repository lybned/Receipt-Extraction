from datasets import load_dataset

class DataUtil:
	def __init__(self):
		self.dataset = load_dataset("naver-clova-ix/cord-v1")
		
	def get_train_data(index):
		return self.dataset['train'][index]
		