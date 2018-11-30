import random

data = [
    [
        {'cost': 100.00, 'fileName': 'test.jpg', 'stated': True, 'statedPrice': 130, 'sequential': True, 'displayRange': 5},
        {'cost': 28.24, 'fileName': '2824.jpg', 'stated': True, 'statedPrice': 30.00, 'sequential': True, 'displayRange': 4},
        {'cost': 379.54, 'fileName': '2824.jpg', 'stated': True, 'statedPrice': 20, 'sequential': True,  'displayRange': 3}
    ]
]

def shuffle(data):
    return[random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)