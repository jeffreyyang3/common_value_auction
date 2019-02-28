import random

data = [
    [   # coins are in order pennies, nickels, dimes. quarters
        {'cost': 100.00, 'fileName': 'test.jpg', 'stated': True, 
        'coins': [20,30,10,12],
        'statedPrice': 130, 'sequential': True, 'displayRange': 5, 'showStats': False,},
        {'cost': 28.24, 'fileName': '2824.jpg', 'stated': False, 'coins': [10,80,10,12],
        'statedPrice': 30.00, 'sequential': True, 'displayRange': 4, 'showStats' : True},
        {'cost': 379.54, 'fileName': '2824.jpg', 'coins' : [100,40,12,12], 'stated': True,
         'statedPrice': 20, 'sequential': False,  'displayRange': 3, 'showStats' : False},
         {'cost': 100.00, 'fileName': 'test.jpg', 'stated': True, 'coins' : [90,40,12,30],
        'statedPrice': 130, 'sequential': True, 'displayRange': 4, 'showStats': True,},
        {'cost': 28.24, 'fileName': '2824.jpg', 'stated': False, 'coins' : [20,40,62,70],
        'statedPrice': 30.00, 'sequential': False, 'displayRange': 5, 'showStats' : False},
        {'cost': 379.54, 'fileName': '2824.jpg', 'stated': True, 'coins' : [20,40,12,100],
         'statedPrice': 20, 'sequential': True,  'displayRange': 2, 'showStats' : True},

    ]
]

def shuffle(data):
    return data
    #return[random.sample(data[0], k=len(data[0]))]

def export_data():
    return shuffle(data)
    