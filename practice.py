# 1. return first repeat occurence Element index
"""-> output = 5"""

arr = [10, 4, 5, 3, 5, 3, 6]

for num in arr:
    if arr.count(num) > 1:
        print(num)
        break


# 2. 1) return batter element where type is Chocolate
#    2) return topping elements where type is include Chocolate

"""
output:-
1){ "id": "1002", "type": "Chocolate" }
2){ "id": "5006", "type": "Chocolate with Sprinkles" }{ "id": "5003", "type": "Chocolate" }
"""

object = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters":
    {
        "batter":
        [
            {"id": "1001", "type": "Regular"},
            {"id": "1002", "type": "Chocolate"},
            {"id": "1003", "type": "Blueberry"},
            {"id": "1004", "type": "Devil's Food"}
        ]
    },
    "topping":
    [
        {"id": "5001", "type": "None"},
        {"id": "5002", "type": "Glazed"},
        {"id": "5005", "type": "Sugar"},
        {"id": "5007", "type": "Powdered Sugar"},
        {"id": "5006", "type": "Chocolate with Sprinkles"},
        {"id": "5003", "type": "Chocolate"},
        {"id": "5004", "type": "Maple"}
    ]
}

# 1st Question answer
print('--------1st question answer------------')
for obj in object['batters']['batter']:
    if obj['type'] == 'Chocolate':
        print(obj)

# 2nd Quetion answer
print('--------2nd question answer------------')
for obj in object['topping']:
    if 'Chocolate' in obj['type']:
        print(obj, end='')

# 3 Question

'''
output:-
[{
    "name" : "mihir",
    "data" : [{"age" : 23}]
},
{
    "name" : "hiren",
    "data" : [{"age" : 21}]
},
{
    "name" : "shashank",
    "data" : [{"age" : 20}]
},
{
    "name" : "vasudha",
    "data" : []
}
]

'''

a = [{
    "name": "mihir",
    "data": []
},
    {
    "name": "hiren",
    "data": []
},
    {
    "name": "shashank",
    "data": []
},
    {
    "name": "vasudha",
    "data": []
}
]


b = {
    "mihir": {"age": 23},
    "hiren": {"age": 21},
    "shashank": {"age": 20},

}
print()
for obj in a:
    if obj['name'] in b:
        obj['data'].append(b[obj['name']])

print(a)
