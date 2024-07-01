import json

with open('points.json') as f:
    points = json.load(f)

def within_1(x, y):
    return 145 <= x <= 165 and 75 <= y <= 225


def within_either_0(x, y, center_x, center_y):
    return 75 ** 2 >= (x - center_x) ** 2 + (y - center_y) ** 2 >= 55 ** 2


def within_0(x, y):
    left_center_x = 250
    right_center_x = 410
    center_y = 150
    return within_either_0(x, y, left_center_x, center_y) or within_either_0(x, y, right_center_x, center_y)


def within_logo(x, y):
    return within_1(x, y) or within_0(x, y)


count = 0
for point in points['coords']:
    x, y = point
    if within_logo(x, y):
        count += 1
print(count)