import json

def load_config(file_name):
    with open(file_name) as rf:
        config = json.load(rf)
    return config
