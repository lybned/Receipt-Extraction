
from src.config import *

from src.Data.DataUtil import *
from src.Image.ImageUtil import *
from src.LLM.LLMUtil import *
from src.MLFlow.MLFlowUtil import *
from src.OCR.OCRUtil import *

import numpy as np
import json

if __name__ == "__main__":
	print("Main Running...")
	data = DataUtil()
	imageU = ImageUtil()
	ocr_model = OCRUtil()
	llm = LLMUtil()	
	mlflow_class = MLFlowUtil()
	
	train_data = data.get_train_data()

	#print(train_data)
	receipt_list = []
	image_list = train_data[:30]["image"]
	truth_list = train_data[:30]["ground_truth"]
	truth_list = list(map(lambda x: json.loads(x), truth_list))
	for i in range(30):
		img = image_list[i]

		new_img = data.darken_image(img)
		img_np = np.array(new_img)		
		receipt = ocr_model.extract_text(new_img)
		receipt_list.append(receipt)
		image_list.append(new_img)
		
	result_list = llm.llm_ask(receipt_list)
	
	# (self,receipt_list, image_list, result, truth_list)
	
	print(len(truth_list))
	for aa in truth_list:
		print(aa)
	mlflow_class.write_result(receipt_list, image_list, result_list, truth_list)