from paddleocr import PaddleOCR
import numpy as np
from src.config import *

def organize_extracted_text(data_array):
	result = ""
	last_cord = None
	for data in data_array:
		if (len(data[1][0]) > minimum_word_length):
			if last_cord == None:
				last_cord = data[0]
				result += data[1][0]
			else:
				if (check_y(data[0], last_cord)):
					result += (" " +data[1][0])
				else:
					result += ("\n" + data[1][0])
				last_cord = data[0]
	return result
	
	
def check_y(array_a, array_b):
	diff_list = []
	for i in range(4):
		diff_list.append(abs(array_a[i][1]-array_b[i][1]))
		if (len(list(filter(lambda x: x<=same_row_threshold , diff_list))) > 1):
			return True
	return False
	
	
class OCRUtil:
	def __init__(self):
		self.model = PaddleOCR(use_angle_cls=True, lang='en')
		
	def extract_text(self,img):
		img_np = np.array(img)
		results = self.model.ocr(img_np, cls=True)
		return organize_extracted_text(results[0])
		
