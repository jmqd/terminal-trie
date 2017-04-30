import json

def get_all_subclasses(cls):
    all_subclasses = []

    for subclass in cls.__subclasses__():
        all_subclasses.append(subclass)
        all_subclasses.extend(get_all_subclasses(subclass))

    return all_subclasses


def load_jsonfile(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config
