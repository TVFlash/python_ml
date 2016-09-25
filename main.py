import json
from pprint import pprint

def json_file_to_object(filepath):
	json_raw = open(filepath, 'r')
	json_data = [json.loads(line) for line in json_raw]
	return json_data

def perform_analytics(json_data):
	return False

if __name__ == '__main__':
	filepath = "yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
	json_data = json_file_to_object(filepath)
	perform_analytics(json_data)

