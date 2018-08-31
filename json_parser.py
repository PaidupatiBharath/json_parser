import json
from numpy import array


def feature_from_json(json_file):
    '''This functions returns a specific element
    of a json record in a single dimensional
    numpy array'''
    with open(json_file) as json_log:
        data = json.load(json_log)

    datarate = []
    interval = data['intervals']
    for elem in interval:
        datarate.append(elem['streams'][0]['bits_per_second'])

    datarate = [x/(1024 * 1024) for x in datarate]
    features = array(datarate)
    return features
