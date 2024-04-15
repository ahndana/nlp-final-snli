import json

dev_path = 'snli_1.0/snli_1.0_dev.jsonl'
train_path = 'snli_1.0/snli_1.0_train.jsonl'
test_path = 'snli_1.0/snli_1.0_test.jsonl'


# creates a dictionary where keys are file paths (train,test,dev) and values are array list of strings [[sentence1,sentence2], [sentence3,sentence4], ...]
path_to_list = {}
path_to_list[train_path] = []
path_to_list[dev_path] = []
path_to_list[test_path] = []

# creates a dictionary where keys are file paths (train,test,dev) and values are labels for each [sentence1,sentence2]
path_to_label = {}
path_to_label[train_path] = []
path_to_label[dev_path] = []
path_to_label[test_path] = []

for path in path_to_list:
    with open(path, 'r') as file:
        for line in file:
            sentence_list = []
            json_data = json.loads(line)
            sentence_list.append(json_data.get('sentence1'))
            sentence_list.append(json_data.get('sentence2'))
            path_to_label[path].append(json_data.get('gold_label'))
            path_to_list[path].append(sentence_list)


