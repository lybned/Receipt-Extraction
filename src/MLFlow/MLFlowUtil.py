
import mlflow
import io
import json
import re

from src.config import *
def replace_dot_except_last(input_string):
    # Split the string by the last occurrence of a dot
    parts = input_string.rsplit('.', 1)
    # Replace all dots in the part before the last one with commas
    parts[0] = parts[0].replace('.', ',')
    # Join the parts back with a dot before the last occurrence
    return '.'.join(parts)

def remove_letters(input_string):
    # Use regular expression to remove all alphabetic characters (a-z and A-Z)
    return re.sub(r'[a-zA-Z]', '', input_string)

def clean_items(items):
    return list(map(lambda x:x.replace(".", ""), items))

def cleanText(text):

    clean_text = text.replace("\\", "")
    clean_text = re.sub(r'"{2,}', '"', clean_text)  
    #clean_text = replace_dot_except_last(clean_text) #.replace( ' ",', ' "",')
    clean_text = clean_text.replace("{", "").replace("}", "")
    if (clean_text.startswith("[")):
        clean_text = clean_text[1:]
    if (clean_text.endswith("]")):
        clean_text = clean_text[:-1]
    return "{" + clean_text.replace('"restaurant_name": ",', '"restaurant_name": "",') + "}"
	
def are_lists_equal(predict, actual):
    # Convert all strings in both lists to lowercase
    lower_predict = [item.lower() for item in predict]
    lower_actual = [item.lower() for item in actual]
    lower_predict.sort()
    lower_actual.sort()
    not_included = []
    print(lower_predict)
    print(lower_actual)
    # Compare the two lists
    for word in lower_actual:
        if (not word in lower_predict):
            not_included.append(word)
    return (len(not_included) == 0, not_included)

def extra_items(ground_truth):
    item_list = []
    #print(ground_truth["gt_parse"]["menu"])
    truth_list = ground_truth["gt_parse"]["menu"] if isinstance(ground_truth["gt_parse"]["menu"], list) else [ground_truth["gt_parse"]["menu"]]
    for ii in truth_list:
        item_list.append(ii["nm"].replace(".", ""))
    return item_list

class MLFlowUtil:
	def __init__(self):
		pass
		
	def write_result(self,receipt_list, image_list, result, truth_list):
		mlflow.set_tracking_uri(uri="http://127.0.0.1:7777/")
		# Create a new MLflow Experiment
		mlflow.set_experiment("OCR Extraction")
		price_correct = {"wrong":0,"correct":0}
		actual_list = []
		predict_list = []
		wrong = []
		truth = []
		predict = []
		item_correct= {"wrong":0,"correct":0}
		wrong_items = {}
		empty_list = []
		print(len(receipt_list))
		# Create a new MLflow Experiment
		with mlflow.start_run():

			mlflow.log_param("Prompt", Prompt_no_original)  
			for i,name in enumerate(receipt_list):
			#with mlflow.start_run(nested=True,run_name="Image Number: "+str(i)):

				mlflow.log_image(image_list[i], f"example_image{i}.png")


				#mlflow.log_param("file_name", i)   
				#mlflow.log_param("extraction",result[i]) 
				#mlflow.log_param("Ground Truth", json.loads(ds['train'][i]['ground_truth'])["gt_parse"])
				#truth.append(json.loads(ds['train'][i]['ground_truth'])["gt_parse"])
				truth.append(truth_list[i]["gt_parse"])
				
				actual_price = float(remove_letters(str(truth_list[i]["gt_parse"]["total"]["total_price"].replace(",", ""))))

				#print("-----------END----------")
				actual_item_list = extra_items(truth_list[i])    

				clean_result =  "}".join(dict(result[i])['raw'].split("}")[:-1]) + "}"

				clean_result = cleanText(clean_result)
				#print("RAW")
				print("-----------START--------")
				print(clean_result)
				print("-----------END----------")  
				#print(json.loads(clean_result)["price"])
				if ("price" in json.loads(clean_result)):
					predict_price = float(replace_dot_except_last(str(json.loads(clean_result)["price"])).replace(",", ""))
					predict_items = clean_items(json.loads(clean_result)["items"])

					if (actual_price == predict_price) :
						price_correct["correct"] += 1
					else:
						price_correct["wrong"] += 1
						wrong.append([predict_price, actual_price,receipt_list[i]])
					compare_item_result = are_lists_equal(predict_items, actual_item_list)
					if (compare_item_result[0]):
						item_correct["correct"] += 1
					else:
						item_correct["wrong"] += 1
						wrong_items[str(i)] = [predict_items, compare_item_result[1]]
					actual_list.append(actual_price)
					predict_list.append(predict_price)
				else:
					empty_list.append([receipt_list[i], i])
				#print("-------------------------")



			#mlflow.log_param("truth", truth)
			#mlflow.log_param("predict", predict)
			mlflow.log_param("minimum_word_length", minimum_word_length)
			mlflow.log_param("same_row_threshold", same_row_threshold)
			mlflow.log_param("actual price list", actual_list)
			mlflow.log_param("predict price list", predict_list)
			mlflow.log_param("price result", price_correct)
			mlflow.log_param("wrong answer", wrong)
			mlflow.log_param("item result", item_correct)
			mlflow.log_param("wrong items", wrong_items)
			mlflow.log_param("no extractions", empty_list)
				