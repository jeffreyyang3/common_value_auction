import random

data = [
    [
        {'cost': 100.00, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 130},
        {'cost': 100.00, 'fileName': 'test.jpg', 'stated': False, 'statedPrice': 120},
        {'cost': 100.00, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 100}
    ]
]

def shuffle(data):
    return[random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)