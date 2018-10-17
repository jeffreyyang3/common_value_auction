import random

data = [
    [
        {'cost': 100, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 130},
        {'cost': 100, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 120},
        {'cost': 100, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 100}
    ]
]

def shuffle(data):
    return[random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)