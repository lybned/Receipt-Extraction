Prompt_no_original = '''
Accurately summarize the items, final price, and restaurant name of the receipt. Have the final answer in a JSON format. The json should contain 3 different attributes: restaurant_name as a string, 
items as a list of strings, and price as a float. 
Make sure to do the following:
- Only keep the item name without getting the price of the item.
- Make sure to use Double Quotes and remove the single quotes. 
- Only one single json should be returned and nothing else. 
- Make sure to include the price in a double quote and make sure the price does NOT contain any special characters in it. The format should be "12344.00".
- If you are unable to extract a certain field, leave is as an empty string.
- No Speical characters in the item name.
- No single quote anywhere in the result.
- Make sure to get the final price NOT the one before discount or tax.
'''

minimum_word_length = 2
same_row_threshold = -2