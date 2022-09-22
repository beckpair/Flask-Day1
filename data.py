import json
import pandas

excel_data_df = pandas.read_excel('book_list.xlsx', sheet_name = 'Sheet1')

thisisjson = excel_data_df.to_json(orient='records')

print('Excel sheet to JSON:\n', thisisjson)

thisisjson_dict = json.loads(thisisjson)

with open('book_list.json', 'w') as json_file:
    json.dump(thisisjson_dict, json_file)