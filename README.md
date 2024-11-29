# Receipt-Extraction

The project involves extract receipt information from an image through the following steps:
- Read images from a targeted dataset
- Transform the image to be more readable
- Apply OCR to extract content
- Make the OCR result into a string.
- Give the cleaned OCR result to a LLM for information extraction.
- Save the results into MLFLOW.

## How to run
- use pip to install all necessary libraries in the requirements.txt.
- Run main.py to run the entire project.
- test.py is used for testing.