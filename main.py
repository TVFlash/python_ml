import json
from pprint import pprint
from sklearn import tree

compound_list = ['Ambience', 'Dietary Restrictions', 'Good For', 'Music', 'Parking' ]
ignore_list = ['Hair Types Specialized In']

def json_file_to_object(filepath):
	json_raw = open(filepath, 'r')
	json_data = [json.loads(line) for line in json_raw]
	return json_data

def perform_analytics(json_data):
	tokens = tokenize_json(json_data)
	classification_and_regression_tree(tokens)

def classification_and_regression_tree(tokens):
	clf = tree.DecisionTreeClassifier()

def tokenize_json(json_data):
	attributes = {}
	for row in json_data:
		for key, value in row['attributes'].iteritems():
			if key in compound_list:
				for sub_key, sub_value in value.iteritems():
					compositeKey = key + "." + sub_key + "." + str(sub_value)
					count_attribute(compositeKey, attributes)
			elif key not in ignore_list:
				compositeKey = key + "." + str(value)
				count_attribute(compositeKey, attributes)
	#pprint(attributes)
	return attributes

def count_attribute(attribute, attributes):
	if attribute not in attributes:
		attributes[attribute] =  1
	else:
		attributes[attribute] += 1

if __name__ == '__main__':
	filepath = "../../Downloads/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
	json_data = json_file_to_object(filepath)
	perform_analytics(json_data)

